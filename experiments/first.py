"""Enumerate edge partitions and emit independently checkable embeddings."""
from pathlib import Path
import sys, json
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'tools'))
from source import checked_source
checked_source()

def partitions(n, word=()):
    if len(word)==n:
        yield word; return
    for a in range(max(word,default=-1)+2):
        yield from partitions(n,word+(a,))

def certificate(n, edges, colors):
    q=max(colors)+1
    coordinates=[]
    for axis in range(q):
        parent=list(range(n))
        def find(u):
            while parent[u]!=u: u=parent[u]
            return u
        for (u,v),a in zip(edges,colors):
            if a!=axis: parent[find(u)]=find(v)
        coordinates.append([find(v) for v in range(n)])
    return [list(x) for x in zip(*coordinates)]

def verify(n, edges, colors, mapping):
    q=max(colors)+1
    return (len(mapping)==n and all(len(v)==q for v in mapping)
            and len(set(map(tuple,mapping)))==n
            and all([a for a in range(q) if mapping[u][a]!=mapping[v][a]]==[color]
                    for (u,v),color in zip(edges,colors))
            and all(len({v[a] for v in mapping})>1 for a in range(q)))

def search(name,n,edges):
    best=None; tested=0; valid=0
    for colors in partitions(len(edges)):
        tested+=1
        mapping=certificate(n,edges,colors)
        if verify(n,edges,colors,mapping):
            valid+=1
            if best is None or max(colors)+1>best['support']:
                best={'support':max(colors)+1,'colors':list(colors),'vertices':mapping}
    assert best
    assert not verify(n,edges,best['colors'],[best['vertices'][0]]*n)
    return {'case':name,'n':n,'edges':edges,'partitions_tested':tested,'valid_partitions':valid,'best':best}

def product(n,e,m,f):
    return n*m, sorted([(u*m+j,v*m+j) for u,v in e for j in range(m)] +
                       [(i*m+u,i*m+v) for i in range(n) for u,v in f])
k2=(2,[(0,1)]); p3=(3,[(0,1),(1,2)]); k3=(3,[(0,1),(0,2),(1,2)])
rows=[search(name,*g) for name,g in [('K2',k2),('P3',p3),('K3',k3),
    ('K2 square K2',product(*k2,*k2)),('K2 square P3',product(*k2,*p3)),
    ('K2 square K3',product(*k2,*k3))]]
assert [r['best']['support'] for r in rows]==[1,2,1,2,3,2]
print(json.dumps({'domain':'all edge partitions of six specified connected graphs',
    'cases':rows,'status':'valid lower-bound certificates; completeness proof and general additivity remain open'},indent=2))
