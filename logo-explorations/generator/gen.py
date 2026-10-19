import math, random, cmath
random.seed(7)
V,G,M,Q='v','g','m','q'

# 1. deep stochastic quadtree, 560x560
rects={V:[],G:[],M:[],Q:[]}
def quad(x,y,s,d):
    p = 0.95 if d<2 else max(0.25, 0.9-0.11*d)
    if s>6 and (d<2 or random.random()<p):
        h=s/2
        for (dx,dy) in ((0,0),(h,0),(0,h),(h,h)):
            quad(x+dx,y+dy,h,d+1)
    else:
        g=1.0 if s<12 else 2.0
        c = random.choices([V,G,Q,M],[50,28,18,4 if s<20 else 0])[0]
        rects[c].append(f"M{x+g:.1f} {y+g:.1f}h{s-2*g:.1f}v{s-2*g:.1f}h{-(s-2*g):.1f}z")
quad(0,0,560,0)
n=sum(len(v) for v in rects.values())
open('quad.txt','w').write("\n".join(f'<path fill="{{{c}}}" d="{"".join(p)}"/>' for c,p in rects.items() if p))
print('quad',n)

# 2. Pythagoras tree, asymmetric, depth 10
polys={V:[],G:[],M:[],Q:[]}
def tree(p1,p2,d,maxd):
    # square on segment p1->p2 (base), growing to the left
    v=p2-p1; n=complex(-v.imag,v.real)
    p3=p2+n; p4=p1+n
    c = M if d==maxd else (V if d%2==0 else G)
    polys[c].append("M"+"L".join(f"{p.real:.1f} {p.imag:.1f}" for p in (p1,p2,p3,p4))+"z")
    if d<maxd:
        a=math.radians(38)
        top=p4+(p3-p4)*cmath.exp(-1j*a)*math.cos(a)
        tree(p4,top,d+1,maxd); tree(top,p3,d+1,maxd)
tree(complex(250,560),complex(390,560),0,10)
n=sum(len(v) for v in polys.values())
open('tree.txt','w').write("\n".join(f'<path fill="{{{c}}}" d="{"".join(p)}"/>' for c,p in polys.items() if p))
print('tree',n)

# 3. Apollonian gasket, radius 280
circs=[]
def gasket():
    R=280.0
    # three inner circles: radii r1,r2 chosen asymmetric
    r1,r2=0.56*R,0.44*R  # tangent: centers distance r1+r2 = R
    c1=complex(-(R-r1),0); c2=complex(R-r2,0)
    # third tangent to outer and both: solve via Descartes
    k0=-1/R; k1=1/r1; k2=1/r2
    def desc(k1,k2,k3,z1,z2,z3,sign):
        k4=k1+k2+k3+sign*2*math.sqrt(max(0,k1*k2+k2*k3+k3*k1))
        if k4==0: return None
        s=k1*z1+k2*z2+k3*z3
        rad=cmath.sqrt(k1*k2*z1*z2+k2*k3*z2*z3+k3*k1*z3*z1)
        for z4 in ((s+2*rad)/k4,(s-2*rad)/k4):
            yield k4,z4
    circs.append((k0,0j)); circs.append((k1,c1)); circs.append((k2,c2))
    cands=list(desc(k0,k1,k2,0j,c1,c2,1))
    # pick the one consistent (tangent to all three)
    def tangent(k,z,trip):
        r=1/k
        for kk,zz in trip:
            rr=1/kk
            if abs(abs(z-zz)-abs(abs(rr)-r))>0.5 and abs(abs(z-zz)-(abs(rr)+r))>0.5: return False
        return True
    trip=[(k0,0j),(k1,c1),(k2,c2)]
    added=[]
    for k,z in cands:
        if k>0 and tangent(k,z,trip): added.append((k,z))
    added=added[:2]
    for a in added: circs.append(a)
    stack=[]
    for a in added:
        for i in range(3):
            t=[trip[j] for j in range(3) if j!=i]+[a]
            stack.append(tuple(t))
    # also the gap between c1,c2 and both new
    if len(added)==2:
        stack.append(((k1,c1),(k2,c2),added[0])); stack.append(((k1,c1),(k2,c2),added[1]))
    seen=set()
    while stack:
        (ka,za),(kb,zb),(kc,zc)=stack.pop()
        for k,z in desc(ka,kb,kc,za,zb,zc,1):
            if k<=0 or 1/k<1.3: continue
            key=(round(z.real,2),round(z.imag,2))
            if key in seen or not tangent(k,z,[(ka,za),(kb,zb),(kc,zc)]): continue
            # reject if overlapping existing
            if any(abs(z-zz)+1e-3 < abs(1/kk)+1/k-0.5 and kk>0 for kk,zz in circs): continue
            seen.add(key); circs.append((k,z))
            stack.append(((ka,za),(kb,zb),(k,z))); stack.append(((ka,za),(kc,zc),(k,z))); stack.append(((kb,zb),(kc,zc),(k,z)))
gasket()
out=[]
for i,(k,z) in enumerate(circs):
    r=abs(1/k)
    if k<0: col=Q
    elif r>60: col=V
    elif r>12: col=G
    elif r>3: col=V
    else: col=M
    out.append(f'<circle cx="{z.real+280:.1f}" cy="{z.imag+280:.1f}" r="{r:.1f}" fill="{{{col}}}"/>' if k>0 else f'<circle cx="280" cy="280" r="{r:.1f}" fill="none" stroke="{{{Q}}}" stroke-width="2"/>')
open('gasket.txt','w').write("\n".join(out)); print('gasket',len(circs))

# 4. dragon curve order 13
turns=[]
for i in range(13):
    turns=turns+[1]+[-t for t in reversed(turns)]
x,y=0,0; d=0; pts=[(0,0)]
dirs=[(1,0),(0,1),(-1,0),(0,-1)]
for t in turns+[0]:
    dx,dy=dirs[d]; x+=dx; y+=dy; pts.append((x,y))
    d=(d+t)%4
xs=[p[0] for p in pts]; ys=[p[1] for p in pts]
mnx,mxx,mny,mxy=min(xs),max(xs),min(ys),max(ys)
sc=560/max(mxx-mnx,mxy-mny)
ox=(560-(mxx-mnx)*sc)/2; oy=(560-(mxy-mny)*sc)/2
def P(p): return f"{(p[0]-mnx)*sc+ox:.1f} {(p[1]-mny)*sc+oy:.1f}"
cut=len(pts)-len(pts)//48
main="M"+"L".join(P(p) for p in pts[:cut+1]); tail="M"+"L".join(P(p) for p in pts[cut:])
open('dragon.txt','w').write(f'<path fill="none" stroke="{{v}}" stroke-width="{sc*0.55:.2f}" stroke-linejoin="round" d="{main}"/>\n<path fill="none" stroke="{{m}}" stroke-width="{sc*0.55:.2f}" stroke-linejoin="round" d="{tail}"/>')
print('dragon',len(pts),sc)

# Colour keys {v} {g} {m} {q} map to violet #a06bff, green #37e8a4, magenta #ff5ad6, hairline #3a2a55.
# Drop each .txt into template.html at __GEOMETRY__ to rebuild an artboard.
