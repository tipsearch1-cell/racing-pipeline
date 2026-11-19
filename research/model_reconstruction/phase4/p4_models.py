"""Phase 4 model algorithms (race-level). All fits take rows sorted by race, with contiguous race groups.

  clogit_fit / clogit_score      : linear race-softmax (conditional logit), optional offset, L2
  ListwiseGBM                    : Newton boosting of the race-softmax loss with regression trees (optional offset)
  PairwiseGBM                    : RankNet-style pairwise logistic boosting on an additive runner score
  temperature_fit                : race-softmax temperature for turning scores into probabilities
"""
import numpy as np
from scipy.optimize import minimize
from sklearn.tree import DecisionTreeRegressor

EPS = 1e-12


def groups(race):
    """race: array of race ids (sorted, contiguous). Returns start indices and group index per row."""
    race = np.asarray(race)
    starts = np.r_[0, np.flatnonzero(race[1:] != race[:-1]) + 1]
    gid = np.zeros(len(race), int); gid[starts[1:]] = 1; gid = np.cumsum(gid)
    return starts, gid


def softmax_g(s, starts, gid):
    m = np.maximum.reduceat(s, starts)
    e = np.exp(s - m[gid])
    z = np.add.reduceat(e, starts)
    return e / z[gid]


def race_ll(p, y, starts):
    """mean over races of -log p(winner)."""
    return -np.log(np.clip(p[y == 1], EPS, 1)).mean()


# ------------------------------------------------------------------ linear conditional logit
def clogit_fit(X, y, race, l2=1.0, offset=None, w0=None):
    starts, gid = groups(race)
    off = np.zeros(len(y)) if offset is None else offset

    def f(w):
        s = off + X @ w
        p = softmax_g(s, starts, gid)
        nll = -np.sum(np.log(np.clip(p[y == 1], EPS, 1)))
        g = X.T @ (p - y)
        return nll + 0.5 * l2 * w @ w, g + l2 * w
    w0 = np.zeros(X.shape[1]) if w0 is None else w0
    r = minimize(f, w0, jac=True, method="L-BFGS-B", options={"maxiter": 500})
    return r.x


def clogit_score(X, w, offset=None):
    return (0 if offset is None else offset) + X @ w


# ------------------------------------------------------------------ listwise boosting
class ListwiseGBM:
    def __init__(self, depth=3, lr=0.05, n_max=300, min_leaf=200, seed=20261119, max_features=None):
        self.depth, self.lr, self.n_max, self.min_leaf, self.seed, self.max_features = depth, lr, n_max, min_leaf, seed, max_features
        self.trees = []

    def fit(self, X, y, race, offset=None, Xv=None, yv=None, racev=None, offv=None, patience=25):
        starts, gid = groups(race)
        s = np.zeros(len(y)) if offset is None else offset.astype(float).copy()
        if Xv is not None:
            sv_st, sv_g = groups(racev)
            sv = np.zeros(len(yv)) if offv is None else offv.astype(float).copy()
        best, best_n, self.trees, self.val_curve = np.inf, 0, [], []
        for t in range(self.n_max):
            p = softmax_g(s, starts, gid)
            g = p - y; h = np.clip(p * (1 - p), 1e-6, None)
            tree = DecisionTreeRegressor(max_depth=self.depth, min_samples_leaf=self.min_leaf, random_state=self.seed + t, max_features=self.max_features)
            tree.fit(X, -g / h, sample_weight=h)
            s += self.lr * tree.predict(X)
            self.trees.append(tree)
            if Xv is not None:
                sv += self.lr * tree.predict(Xv)
                ll = race_ll(softmax_g(sv, sv_st, sv_g), yv, sv_st)
                self.val_curve.append(ll)
                if ll < best - 1e-6:
                    best, best_n = ll, t + 1
                elif t + 1 - best_n >= patience:
                    break
        if Xv is not None:
            self.trees = self.trees[:max(best_n, 1)]
        return self

    def score(self, X, offset=None):
        s = np.zeros(X.shape[0]) if offset is None else offset.astype(float).copy()
        for tr in self.trees:
            s += self.lr * tr.predict(X)
        return s


# ------------------------------------------------------------------ pairwise boosting (RankNet on an additive score)
def make_pairs(pos, race, rng, k_other=5):
    """Pairs (better, worse) within races: winner vs every other runner, plus up to k_other sampled finisher pairs."""
    starts, _ = groups(race)
    ends = np.r_[starts[1:], len(race)]
    A, B = [], []
    for a, b in zip(starts, ends):
        idx = np.arange(a, b); pp = pos[a:b]
        fin = np.isfinite(pp)
        w = idx[pp == 1]
        if len(w) != 1:
            continue
        others = idx[idx != w[0]]
        A += [w[0]] * len(others); B += list(others)
        fi = idx[fin & (pp > 1)]
        if len(fi) >= 2:
            for _ in range(min(k_other, len(fi))):
                i, j = rng.choice(fi, 2, replace=False)
                if pos[i] < pos[j]:
                    A.append(i); B.append(j)
                elif pos[j] < pos[i]:
                    A.append(j); B.append(i)
            nf = idx[~fin]
            for j in nf[:2]:       # non-finishers behind a sampled finisher
                A.append(rng.choice(fi)); B.append(j)
    return np.array(A), np.array(B)


class PairwiseGBM:
    def __init__(self, depth=3, lr=0.1, n_max=200, min_leaf=200, seed=20261119, max_features=None):
        self.depth, self.lr, self.n_max, self.min_leaf, self.seed, self.max_features = depth, lr, n_max, min_leaf, seed, max_features

    def fit(self, X, pos, race, Xv=None, yv=None, racev=None, patience=20):
        rng = np.random.default_rng(self.seed)
        A, B = make_pairs(pos, race, rng)
        s = np.zeros(X.shape[0]); self.trees = []
        if Xv is not None:
            st, gg = groups(racev); sv = np.zeros(Xv.shape[0])
        best, best_n = np.inf, 0
        for t in range(self.n_max):
            d = s[A] - s[B]
            sig = 1 / (1 + np.exp(d))                   # dLoss/d(s_A) = -sig
            g = np.zeros_like(s); h = np.zeros_like(s)
            np.add.at(g, A, -sig); np.add.at(g, B, sig)
            hh = sig * (1 - sig); np.add.at(h, A, hh); np.add.at(h, B, hh)
            used = h > 0
            tree = DecisionTreeRegressor(max_depth=self.depth, min_samples_leaf=self.min_leaf, random_state=self.seed + t, max_features=self.max_features)
            tree.fit(X[used], -g[used] / np.clip(h[used], 1e-6, None), sample_weight=h[used])
            s += self.lr * tree.predict(X)
            self.trees.append(tree)
            if Xv is not None:
                sv += self.lr * tree.predict(Xv)
                a = temperature_fit(sv, yv, racev)
                ll = race_ll(softmax_g(a * sv, st, gg), yv, st)
                if ll < best - 1e-6:
                    best, best_n = ll, t + 1
                elif t + 1 - best_n >= patience:
                    break
        if Xv is not None:
            self.trees = self.trees[:max(best_n, 1)]
        return self

    def score(self, X):
        s = np.zeros(X.shape[0])
        for tr in self.trees:
            s += self.lr * tr.predict(X)
        return s


def temperature_fit(s, y, race):
    starts, gid = groups(race)
    def f(a):
        return -np.sum(np.log(np.clip(softmax_g(a[0] * s, starts, gid)[y == 1], EPS, 1)))
    return float(minimize(f, [1.0], method="L-BFGS-B", bounds=[(0.01, 50)]).x[0])
