"""Live check: python3 tools/livecheck.py DAY <saved racecards file> - flags NRs, going changes, abandonments in bot-bet races vs the sealed card."""
import json,re,sys,csv,gzip
day,live=sys.argv[1],sys.argv[2]
R='/home/claude/racing-pipeline/store/'+day
def load(p):
    t=open(p).read(); 
    try: d=json.loads(t)
    except: d=json.loads(t[t.index('{'):])
    return d.get('racecards',d)
def base(h): return re.sub(r'\s*\([A-Z]{2,3}\)$','',h).strip().lower()
seal=json.load(gzip.open(R+'/sealed_card.json.gz')); seal=seal.get('racecards',seal)
now=load(live)
key=lambda r:(r['course'],r['off_dt'][11:16])
S={key(r):r for r in seal}; N={key(r):r for r in now}
bets=list(csv.DictReader(open(R+f'/reviewer_bets_{day}.csv')))
mult=list(csv.DictReader(open(R+f'/multiples_{day}.csv')))
want=[(b['Course'],b['StartTime'][11:16],b['SelectionName'],'bot') for b in bets]
print('multiples cols',list(mult[0].keys()) if mult else None)
for k,(c,t,h,src) in enumerate(want):
    pass
races={(c,t) for c,t,_,_ in want}
import collections
for (c,t) in sorted(races, key=lambda x:x[1]):
    s=S.get((c,t)); n=None
    for kk,r in N.items():
        if kk[0]==c and kk[1]==t: n=r
    if n is None: print('MISSING race now',c,t); continue
    flags=[]
    if n.get('is_abandoned') or str(n.get('race_status','')).lower() in('abandoned',): flags.append('ABANDONED')
    if s and s.get('going')!=n.get('going'): flags.append(f"going {s.get('going')} -> {n.get('going')}")
    sn={base(x['horse']) for x in s['runners']} if s else set()
    nn={base(x['horse']) for x in n['runners']}
    gone=sn-nn
    if gone: flags.append('NR: '+', '.join(sorted(gone)))
    for cc,tt,h,_ in want:
        if (cc,tt)==(c,t) and base(h) not in nn: flags.append(f'SELECTION NR {h}')
    print(c,t,'|','; '.join(flags) if flags else 'ok')
