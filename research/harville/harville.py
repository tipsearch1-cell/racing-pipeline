"""Harville / discounted Harville / stage-weighted Plackett-Luce finishing-position probabilities (research only).

Sequential selection: stage 1 picks the winner with probability p_i; stage k >= 2 picks from the runners left with
probability w_k,i / sum(w_k over runners left). Plain Harville: w_k = p for every k. Discounted Harville: w_2 = p^a,
w_3 = p^b (stage 4+ reuses the stage-3 weights). The learned model supplies w_k = exp(X theta_k).

All results are exact (no simulation): position probabilities up to 4th are computed with order-n^3 tensors.
Inputs are clipped at EPS and renormalised so every runner keeps a tiny positive weight (no division by zero).
"""
import numpy as np

EPS = 1e-6


def clean(p):
    p = np.asarray(p, dtype=float)
    if p.ndim != 1 or len(p) < 1 or not np.all(np.isfinite(p)) or np.any(p < 0):
        raise ValueError("win probabilities must be a finite, nonnegative 1-d array")
    if p.sum() <= 0:
        raise ValueError("win probabilities sum to zero")
    p = np.clip(p / p.sum(), EPS, None)
    return p / p.sum()


def discount_weights(p, a=1.0, b=1.0):
    p = clean(p)
    lp = np.log(p)
    return p, np.exp(a * lp), np.exp(b * lp)


def position_probs(p, w2=None, w3=None, w4=None, kmax=3):
    """n x kmax matrix: [i, k-1] = P(runner i finishes k-th). kmax <= 4 and kmax <= n."""
    p = clean(p)
    n = len(p)
    w2 = p if w2 is None else np.asarray(w2, float)
    w3 = w2 if w3 is None else np.asarray(w3, float)
    w4 = w3 if w4 is None else np.asarray(w4, float)
    kmax = min(kmax, n)
    out = np.zeros((n, kmax))
    out[:, 0] = p
    if kmax < 2:
        return out
    I = np.eye(n, dtype=bool)
    # T2[j, l] = P(j 1st, l 2nd)
    W2 = w2.sum()
    T2 = p[:, None] * w2[None, :] / (W2 - w2[:, None])
    T2[I] = 0
    out[:, 1] = T2.sum(axis=0)
    if kmax < 3:
        return out
    # T3[j, l, m] = P(j, l, m first three)
    W3 = w3.sum()
    den3 = W3 - w3[:, None] - w3[None, :]
    with np.errstate(divide="ignore", invalid="ignore"):
        T3 = T2[:, :, None] * w3[None, None, :] / den3[:, :, None]
    mask3 = I[:, :, None] | I[:, None, :] | I[None, :, :]
    T3[mask3] = 0
    T3 = np.nan_to_num(T3)
    out[:, 2] = T3.sum(axis=(0, 1))
    if kmax < 4:
        return out
    W4 = w4.sum()
    s = w4[:, None, None] + w4[None, :, None] + w4[None, None, :]
    with np.errstate(divide="ignore", invalid="ignore"):
        R = np.where(mask3, 0.0, T3 / (W4 - s))
    R = np.nan_to_num(R)
    g = R.sum()
    h = R.sum(axis=(1, 2)) + R.sum(axis=(0, 2)) + R.sum(axis=(0, 1))  # each i appears in exactly one slot of a valid triple
    out[:, 3] = w4 * (g - h)
    return out


def top_k(P, k):
    k = min(k, P.shape[1])
    return P[:, :k].sum(axis=1)


def ordered_prob(p, order, w2=None, w3=None):
    """P(the runners in `order` (indices) finish in exactly that order in the first len(order) places)."""
    p = clean(p)
    w2 = p if w2 is None else np.asarray(w2, float)
    w3 = w2 if w3 is None else np.asarray(w3, float)
    pr = p[order[0]]
    if len(order) >= 2:
        pr *= w2[order[1]] / (w2.sum() - w2[order[0]])
    if len(order) >= 3:
        pr *= w3[order[2]] / (w3.sum() - w3[order[0]] - w3[order[1]])
    if len(order) >= 4:
        raise ValueError("ordered_prob supports up to 3 places")
    return pr


def exacta_matrix(p, w2=None):
    p = clean(p)
    w2 = p if w2 is None else np.asarray(w2, float)
    T = p[:, None] * w2[None, :] / (w2.sum() - w2[:, None])
    np.fill_diagonal(T, 0)
    return T
