import json, sys
def load(p):
    d=json.load(open(p))
    papers=[]
    for i,x in enumerate(d.get("papers",[])):
        qs=x.get("questions",[])
        serves=set()
        for q in qs: serves.update(q.get("serves",[]))
        papers.append({"rank":i+1,"paper":x.get("subatlas_paper"),"nq":len(qs),
                       "labels":{q.get("subatlas_cell_label") for q in qs},"serves":serves})
    ao={a.get("cell_label") for a in d.get("atlas_only",[])}
    nr={n.get("subatlas_paper") for n in d.get("not_reading",[])}
    return d,papers,ao,nr
A,pa,aoa,nra=load(sys.argv[1]); B,pb,aob,nrb=load(sys.argv[2])
na,nb=sys.argv[3],sys.argv[4]
print(f"{'':34} {na:>10} {nb:>10}")
print(f"{'papers read':34} {len(pa):>10} {len(pb):>10}")
print(f"{'questions':34} {sum(p['nq'] for p in pa):>10} {sum(p['nq'] for p in pb):>10}")
print(f"{'atlas_only':34} {len(aoa):>10} {len(aob):>10}")
print(f"{'not_reading':34} {len(nra):>10} {len(nrb):>10}")
print("\n-- reading order --")
ra={p['paper']:p for p in pa}; rb={p['paper']:p for p in pb}
for p in sorted(set(ra)|set(rb), key=lambda k: ra.get(k,{}).get('rank',99)):
    a=ra.get(p); b=rb.get(p)
    f=lambda x: f"#{x['rank']} ({x['nq']}q)" if x else "not read"
    flag="" if (a and b and a['rank']==b['rank']) else "   <-- differs"
    print(f"  {p[:44]:46} {f(a):>12} {f(b):>12}{flag}")
print("\n-- per-paper label sets --")
for p in sorted(set(ra)&set(rb), key=lambda k: ra[k]['rank']):
    only_a=ra[p]['labels']-rb[p]['labels']; only_b=rb[p]['labels']-ra[p]['labels']
    if only_a or only_b:
        print(f"  {p}")
        if only_a: print(f"     {na} only: {sorted(only_a)}")
        if only_b: print(f"     {nb} only: {sorted(only_b)}")
print("\n-- atlas_only membership --")
print(f"  {na} only: {sorted(aoa-aob)}")
print(f"  {nb} only: {sorted(aob-aoa)}")
print(f"  agreed  : {len(aoa&aob)}")
print("\n-- coverage check --")
for nm,papers,ao in ((na,pa,aoa),(nb,pb,aob)):
    served=set().union(*[p['serves'] for p in papers]) if papers else set()
    print(f"  {nm}: served {len(served)}, atlas_only {len(ao)}, union {len(served|ao)}, overlap {len(served&ao)}")
