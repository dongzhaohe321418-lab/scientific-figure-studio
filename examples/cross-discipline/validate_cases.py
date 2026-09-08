"""Selected invariants of these four illustrative SVGs, not a general science verifier."""
from pathlib import Path
from collections import Counter
import json, math, re, xml.etree.ElementTree as ET

BASE = Path(__file__).parent
CASES = ['chemistry-sn2','earth-confined-aquifer','ecology-carbon','research-causal-dags']
NS = {'s':'http://www.w3.org/2000/svg'}
def numbers(s): return [float(x) for x in re.findall(r'-?\d+(?:\.\d+)?',s)]
def node(root,id): return next(e for e in root.iter() if e.get('id')==id)
def path(root,id): return node(root,id).find('s:path',NS)
def words(root,id): return ''.join(node(root,id).itertext())
def path_tail(d):
    current=(0.,0.); previous=current
    for command,values in re.findall(r'([MLHVQC])([^MLHVQC]*)',d):
        n=numbers(values); previous=current
        if command=='H': current=(n[-1],current[1])
        elif command=='V': current=(current[0],n[-1])
        else:
            current=tuple(n[-2:])
            if command in 'QC': previous=tuple(n[-4:-2])
    return current,previous
def arrow_valid(g):
    heads = g.findall('s:polygon',NS)
    p = g.find('s:path',NS)
    if len(heads)!=1 or p is None: return False
    points = numbers(heads[0].get('points',''))
    n = numbers(p.get('d',''))
    if len(points)!=6 or len(n)<3: return False
    # All tested scientific arrow paths end with an explicit x,y coordinate.
    end,previous = path_tail(p.get('d','')); tip=points[:2]; back=[(points[2]+points[4])/2,(points[3]+points[5])/2]
    tangent=[end[i]-previous[i] for i in range(2)]
    return math.dist(end,tip)<.02 and sum((tip[i]-back[i])*tangent[i] for i in range(2))>0

def cubic_y(segments,x):
    for pts in segments:
        if pts[0][0] <= x <= pts[-1][0]:
            lo,hi=0.,1.
            def value(t,k): return sum(a*pts[i][k] for i,a in enumerate([(1-t)**3,3*(1-t)**2*t,3*(1-t)*t*t,t**3]))
            for _ in range(60):
                mid=(lo+hi)/2
                if value(mid,0)<x: lo=mid
                else: hi=mid
            return value((lo+hi)/2,1)
    raise ValueError('x outside curve')

def open_path(seq,edges,conditioned):
    # Sufficient for these three-node paths (no descendants of colliders).
    for a,b,c in zip(seq,seq[1:],seq[2:]):
        collider=(a,b) in edges and (c,b) in edges
        if collider and b not in conditioned: return False
        if not collider and b in conditioned: return False
    return True

def validate(slug,root):
    checks={}
    def record(name,value): checks[name]=bool(value)
    if slug=='chemistry-sn2':
        counts={s:Counter(e.get('data-element') for e in root.iter() if e.get('data-state')==s) for s in ['reactant','transition','product']}
        record('atom conservation, including hydroxyl hydrogen',all(c==Counter({'C':1,'H':4,'O':1,'Br':1}) for c in counts.values()))
        record('visible formal charge −1 on both sides and TS',words(root,'r-minus')=='−' and words(root,'p-minus')=='−' and words(root,'ts-charge')=='‡−')
        partials=[e.get('id') for e in root.iter() if e.get('data-bond')=='partial']
        record('only two partial axial bonds',set(partials)=={'t-form','t-break'} and len(partials)==2)
        for id,start in [('electron-attack',(274,923)),('electron-departure',(646,960))]:
            g=node(root,id); record(id+' single head, correct orientation and origin',arrow_valid(g) and numbers(path(root,id).get('d'))[:2]==list(start))
        record('attack originates at selected oxygen pair',math.dist(numbers(path(root,'electron-attack').get('d'))[:2],(274,923))<1)
        record('departing pair starts on C–Br bond',numbers(path(root,'electron-departure').get('d'))[:2]==[646,960] and numbers(path(root,'e-cbr-bond').get('d'))==[602,960,690])
        record('achiral scope explicitly disclosed','not a chiral example' in words(root,'footer'))
    elif slug=='earth-confined-aquifer':
        # Read actual drawn boundaries, not the convenient metadata on standpipe.
        bed=path(root,'aquifer').get('d'); b=numbers(bed)
        roof=[[(b[0],b[1]),(b[2],b[3]),(b[4],b[5]),(b[6],b[7])],[(b[6],b[7]),(b[8],b[9]),(b[10],b[11]),(b[12],b[13])]]
        # Reverse the two backwards cubic segments along the bed floor.
        floor=[[(b[26],b[27]),(b[24],b[25]),(b[22],b[23]),(b[20],b[21])],[(b[20],b[21]),(b[18],b[19]),(b[16],b[17]),(b[14],b[15])]]
        group=node(root,'standpipe'); rects=group.findall('s:rect',NS); casing,water=rects
        cx=float(casing.get('x'))+float(casing.get('width'))/2
        groundnums=numbers(path(root,'land-surface').get('d'))
        ground=[list(zip(groundnums[:8:2],groundnums[1:8:2])),[(groundnums[6],groundnums[7]),(groundnums[8],groundnums[9]),(groundnums[10],groundnums[11]),(groundnums[12],groundnums[13])]]
        head=numbers(path(root,'static-head-line').get('d'))[1]
        screen=[numbers(p.get('d'))[1] for p in group.findall('s:path',NS) if p.get('stroke')=='#455f72']
        record('water surface aligns with local static head',float(water.get('y'))==head)
        record('rim > head > land > aquifer roof in physical elevation',float(casing.get('y'))<head<cubic_y(ground,cx)<cubic_y(roof,cx))
        record('all actual screen slits inside aquifer',len(screen)==8 and all(cubic_y(roof,cx)<y<cubic_y(floor,cx) for y in screen))
        record('outcrop touches land at elevated left boundary',b[:2]==groundnums[:2] and b[1]<head)
        for e in root.iter():
            if e.get('data-species')=='groundwater':
                p=numbers(e.find('s:path',NS).get('d')); record(e.get('id')+' travels inside saturated bed',arrow_valid(e) and all(cubic_y(roof,x)<y<cubic_y(floor,x) for x,y in zip(p[::2],p[1::2])))
    elif slug=='ecology-carbon':
        expected=Counter([('atmosphere','plants'),('plants','atmosphere'),('plants','herbivore'),('herbivore','atmosphere'),('plants','soil'),('herbivore','soil'),('soil','microbes'),('microbes','atmosphere'),('microbes','soil')])
        arrows=[e for e in root.iter() if e.get('data-species')=='carbon']
        record('all nine specified carbon transfers, no extras',Counter((e.get('data-source'),e.get('data-destination')) for e in arrows)==expected)
        record('single correctly oriented head per carbon transfer',all(arrow_valid(e) for e in arrows))
        energies=[e for e in root.iter() if e.get('data-species')=='energy']
        record('solar energy separate from carbon',len(energies)==1 and energies[0].get('data-source')=='sun' and energies[0].get('data-destination')=='plants')
        record('partial budget scope visible','not a complete carbon budget' in words(root,'footer'))
    elif slug=='research-causal-dags':
        expected={'confounder':{('Z','X'),('Z','Y'),('X','Y')},'mediator':{('X','M'),('M','Y'),('X','Y')},'collider':{('X','C'),('Y','C')}}
        for name,edges in expected.items():
            groups=[e for e in root.iter() if e.get('data-graph')==name and e.get('data-species')=='causal-assumption']
            actual={(e.get('data-source'),e.get('data-destination')) for e in groups}
            record(name+' edge set and arrowheads',actual==edges and len(groups)==len(edges) and all(arrow_valid(e) for e in groups))
            remaining=set(actual)
            while remaining:
                origins={a for a,b in remaining}-{b for a,b in remaining}
                if not origins: break
                remaining={(a,b) for a,b in remaining if a not in origins}
            record(name+' acyclic',not remaining)
        record('selected backdoor path blocked by Z',open_path(['X','Z','Y'],expected['confounder'],set()) and not open_path(['X','Z','Y'],expected['confounder'],{'Z'}))
        record('selected mediated path blocked by M',open_path(['X','M','Y'],expected['mediator'],set()) and not open_path(['X','M','Y'],expected['mediator'],{'M'}))
        record('collider path opens on conditioning C',not open_path(['X','C','Y'],expected['collider'],set()) and open_path(['X','C','Y'],expected['collider'],{'C'}))
        record('direct path persists in first two graphs',all(open_path(['X','Y'],expected[n],{z}) for n,z in [('confounder','Z'),('mediator','M')]))
    else: raise ValueError(slug)
    return {'case':slug,'passed':all(checks.values()),'checks':checks,'scope':'Selected illustration-specific invariants; not independent scientific review, empirical verification or a general domain validator.'}

if __name__=='__main__':
    failed=False
    for slug in CASES:
        result=validate(slug,ET.parse(BASE/slug/'figure.svg').getroot())
        (BASE/slug/'scientific-check.json').write_text(json.dumps(result,indent=2,ensure_ascii=False)+'\n',encoding='utf-8',newline='\n')
        print(json.dumps(result,ensure_ascii=False)); failed |= not result['passed']
    raise SystemExit(int(failed))
