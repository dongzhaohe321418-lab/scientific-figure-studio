"""Original editable reconstruction of an inspected image2 endocytosis master.
No third-party image pixels or embedded raster assets. Standard-library only.
"""
import math
from pathlib import Path
from xml.sax.saxutils import escape

OUT = Path(__file__).resolve().parent
parts = []
def add(s): parts.append(s)
def group(id, label, transform=''):
    add(f'<g id="{id}" data-editable="true" data-label="{escape(label)}" transform="{transform}">')
def end(): add('</g>')
def text(id, x, y, label, size=22, weight=400, anchor='start', fill='#253641'):
    add(f'<text id="{id}" data-editable="true" data-label="{escape(label)}" x="{x}" y="{y}" font-size="{size}" font-weight="{weight}" text-anchor="{anchor}" fill="{fill}">{escape(label)}</text>')
def path(d, stroke, width=2, fill='none', extra=''):
    add(f'<path d="{d}" fill="{fill}" stroke="{stroke}" stroke-width="{width}" stroke-linecap="round" stroke-linejoin="round" {extra}/>')
def circle(x,y,r,fill,stroke='none',sw=1):
    add(f'<circle cx="{x:.3f}" cy="{y:.3f}" r="{r}" fill="{fill}" stroke="{stroke}" stroke-width="{sw}"/>')
def curve(p0,p1,p2,p3,n=50):
    return [((1-t)**3*p0[0]+3*(1-t)**2*t*p1[0]+3*(1-t)*t*t*p2[0]+t**3*p3[0],(1-t)**3*p0[1]+3*(1-t)**2*t*p1[1]+3*(1-t)*t*t*p2[1]+t**3*p3[1]) for t in [i/n for i in range(n+1)]]
def sample(points,spacing):
    result=[]; remaining=0.
    for (ax,ay),(bx,by) in zip(points,points[1:]):
        dx,dy=bx-ax,by-ay; length=math.hypot(dx,dy)
        if length==0: continue
        while remaining<length:
            t=remaining/length
            result.append((ax+t*dx,ay+t*dy,-dy/length,dx/length))
            remaining+=spacing
        remaining-=length
    return result
def membrane(id,points,closed=False):
    group(id,'Lipid bilayer')
    d='M '+' L '.join(f'{x:.2f},{y:.2f}' for x,y in points)+(' Z' if closed else '')
    path(d,'#f9ddd0',24)
    for x,y,nx,ny in sample(points,10):
        tx,ty=ny,-nx
        for side in [-1,1]:
            for offset in [-1.6,1.6]:
                start=(x+side*nx*8+tx*offset,y+side*ny*8+ty*offset)
                stop=(x+side*nx*0.9+tx*(offset+1),y+side*ny*.9+ty*(offset+1))
                path(f'M {start[0]:.2f},{start[1]:.2f} L {stop[0]:.2f},{stop[1]:.2f}', '#c68a6f',1.1)
            circle(x+side*nx*12,y+side*ny*12,3.9,'url(#lipid)','#aa5141',.9)
    end()
def receptor(id,x,y,rotation=0,scale=1,cargo=True):
    group(id,'Cargo-bound receptor' if cargo else 'Receptor',f'translate({x} {y}) rotate({rotation}) scale({scale})')
    path('M 0,-37 L 0,28','#145761',6)
    path('M 0,-37 L 0,28','#80b6b7',1.3)
    path('M -10,-46 C -17,-57 -12,-68 0,-68 C 12,-68 17,-57 10,-46 C 7,-42 7,-37 10,-33 C 13,-26 4,-21 0,-23 C -6,-20 -14,-26 -10,-33 C -7,-38 -7,-42 -10,-46 Z','#145761',1.6,'url(#protein)')
    if cargo: circle(0,-81,13.3,'url(#cargo)','#a93e31',1.2)
    end()
def adaptor(id,x,y,rotation=0):
    group(id,'AP2 adaptor',f'translate({x} {y}) rotate({rotation})')
    path('M 0,-11 C -5,-15 -8,-10 -6,-4 L -7,2 L -16,9 C -21,15 -16,19 -10,15 L 0,9 L 10,15 C 16,19 21,15 16,9 L 7,2 L 6,-4 C 8,-10 5,-15 0,-11 Z','#41618f',1.4,'url(#ap2)')
    end()
def triskelion(id,x,y,r=20,rotation=0):
    group(id,'Released clathrin triskelion',f'translate({x} {y}) rotate({rotation})')
    for angle in [0,120,240]:
        a=math.radians(angle); b=math.radians(angle+30)
        px,py=r*.65*math.cos(a),r*.65*math.sin(a)
        qx,qy=px+r*.55*math.cos(b),py+r*.55*math.sin(b)
        path(f'M 0,0 L {px},{py} L {qx},{qy}','#a67225',5)
        path(f'M 0,0 L {px},{py} L {qx},{qy}','#e9b75d',2.3)
        circle(qx,qy,4.5,'url(#coat)','#a67225',1)
    circle(0,0,5.5,'url(#coat)','#a67225',1)
    end()
def coat(id,cx,cy,r,start=0,stop=360,n=14):
    group(id,'Clathrin coat (schematic lattice)')
    angles=[math.radians(start+(stop-start)*i/n) for i in range(n+1)]
    ring=[(cx+r*math.cos(a),cy+r*math.sin(a)) for a in angles]
    inner=[(cx+(r-19)*math.cos(a+(angles[1]-angles[0])*.5),cy+(r-19)*math.sin(a+(angles[1]-angles[0])*.5)) for a in angles[:-1]]
    for i in range(n):
        x,y=ring[i]; xx,yy=ring[i+1]; ix,iy=inner[i]
        d=f'M {x},{y} L {xx},{yy} M {x},{y} L {ix},{iy} L {xx},{yy}'
        path(d,'#ab7629',4.6); path(d,'#e8b65c',2.2)
    for x,y in ring[:-1]: circle(x,y,6.2,'url(#coat)','#a67225',1.2)
    end()
def arrow(id,x1,y1,x2,y2):
    group(id,'Process progression arrow')
    path(f'M {x1},{y1} L {x2},{y2}','#27383e',3,extra='marker-end="url(#arrow)"')
    end()
def ringpoints(cx,cy,r):
    return [(cx+r*math.cos(i*math.tau/180),cy+r*math.sin(i*math.tau/180)) for i in range(181)]

add('''<svg xmlns="http://www.w3.org/2000/svg" width="1920" height="1040" viewBox="0 0 1920 1040" font-family="Arial, Helvetica, sans-serif">
<title>Clathrin-mediated endocytosis</title><desc>Original conceptual mammalian pathway. Editable lipid bilayers, receptors, cargo, AP2, clathrin and dynamin. Cargo remains lumenal; coat proteins are cytosolic. Selected factors shown, not to scale.</desc>
<defs>
<radialGradient id="cargo" cx="30%" cy="25%" r="80%"><stop stop-color="#ffe7d4"/><stop offset=".42" stop-color="#e98c73"/><stop offset="1" stop-color="#bf493a"/></radialGradient>
<radialGradient id="lipid" cx="35%" cy="25%"><stop stop-color="#fff1df"/><stop offset="1" stop-color="#dc8b70"/></radialGradient>
<linearGradient id="protein"><stop stop-color="#215e67"/><stop offset=".5" stop-color="#69a8ac"/><stop offset="1" stop-color="#246570"/></linearGradient>
<linearGradient id="ap2"><stop stop-color="#789dcb"/><stop offset=".45" stop-color="#bbd4eb"/><stop offset="1" stop-color="#6588bc"/></linearGradient>
<radialGradient id="coat" cx="30%" cy="25%"><stop stop-color="#fff0c3"/><stop offset=".5" stop-color="#e6b258"/><stop offset="1" stop-color="#b17c2c"/></radialGradient>
<linearGradient id="dynamin"><stop stop-color="#663650"/><stop offset=".5" stop-color="#b7799a"/><stop offset="1" stop-color="#783e60"/></linearGradient>
<marker id="arrow" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse"><path d="M 0 0 L 10 5 L 0 10 Z" fill="#27383e"/></marker>
</defs><rect width="1920" height="1040" fill="#ffffff"/>
''')
text('title',960,67,'Clathrin-mediated endocytosis',43,600,'middle','#172d35')
text('subtitle',960,110,'Cargo capture, membrane scission and coat removal',24,400,'middle','#4e6169')
for id,x,label in [('a',60,'Cargo capture'),('b',540,'Bud maturation'),('c',1030,'Vesicle scission'),('d',1510,'Uncoating')]:
    text('panel-'+id,x,193,id,34,700)
    text('panel-title-'+id,x+36,190,label,27,600)
text('extracellular',60,262,'Extracellular',20,400,fill='#6b777b')
text('cytosol',60,560,'Cytosol',20,400,fill='#6b777b')

# a: open shallow pit. All cargo above the outer leaflet; coat below.
pa=curve((60,350),(180,350),(175,378),(260,378))+curve((260,378),(345,378),(350,350),(465,350))[1:]
membrane('bilayer-a',pa)
for i,x in enumerate([202,265,328]):
    y=375 if i!=1 else 378
    receptor('receptor-a-'+str(i),x,y)
    adaptor('ap2-a-'+str(i),x,y+37)
group('coat-a','Clathrin coat')
path('M 160,439 Q 266,495 369,439','#a67225',5)
path('M 160,439 Q 266,495 369,439','#e6b258',2.2)
for x,y in [(177,446),(220,461),(264,467),(308,461),(351,446)]:
    path(f'M {x},{y} l -7,-23 M {x},{y} l 13,-16','#c29342',4)
    circle(x,y,6,'url(#coat)','#a67225',1)
end()

# b: open neck, lumen continuous with extracellular space.
pb=[(548,350),(668,350)]+curve((668,350),(726,350),(727,355),(727,394))[1:]+curve((727,394),(727,431),(653,440),(653,529))[1:]+curve((653,529),(653,675),(867,675),(867,529))[1:]+curve((867,529),(867,440),(793,431),(793,394))[1:]+curve((793,394),(793,355),(794,350),(852,350))[1:]+[(971,350)]
membrane('bilayer-b',pb)
coat('coat-b',760,521,150,-37,217,13)
for i,angle in enumerate([45,90,135]):
    a=math.radians(angle)
    tx,ty=760+112*math.cos(a),521+112*math.sin(a)
    x,y,nx,ny=min(sample(pb,2),key=lambda p:(p[0]-tx)**2+(p[1]-ty)**2)
    rotation=math.degrees(math.atan2(ny,nx))-90
    receptor('receptor-b-'+str(i),x,y,rotation,.78)
    adaptor('ap2-b-'+str(i),x+27*nx,y+27*ny,rotation)
group('dynamin-b','Dynamin neck collar')
for y in [376,365,354]:
    add(f'<ellipse cx="760" cy="{y}" rx="40" ry="10" fill="none" stroke="#5a304c" stroke-width="9"/>')
    add(f'<ellipse cx="760" cy="{y-1}" rx="40" ry="10" fill="none" stroke="url(#dynamin)" stroke-width="5.5"/>')
end()
text('dynamin-label',861,271,'Dynamin',20)
group('dynamin-leader','Dynamin leader');path('M 850,277 L 817,277 L 781,342','#52646a',1.5);end()
text('gtp-label',760,722,'GTP-dependent scission',20,400,'middle')

# c and d: closed vesicles, disconnected from a resealed surface membrane.
for panel,cx,left,right in [('c',1213,1035,1404),('d',1668,1506,1850)]:
    membrane('surface-'+panel,[(left,314),(right,314)])
    membrane('vesicle-'+panel,ringpoints(cx,523,107),True)
    for i,angle in enumerate([35,90,145]):
        a=math.radians(angle)
        receptor('receptor-'+panel+'-'+str(i),cx+107*math.cos(a),523+107*math.sin(a),angle-90,.78)
        if panel=='c': adaptor('ap2-c-'+str(i),cx+134*math.cos(a),523+134*math.sin(a),angle-90)
coat('coat-c',1213,523,153,n=15)
text('coated-vesicle',1213,722,'Coated vesicle',20,400,'middle')
for i,(x,y,rot) in enumerate([(1840,558,20),(1852,623,60),(1802,685,0)]):
    triskelion('released-clathrin-'+str(i),x,y,21,rot)
group('uncoating-arrow','Outward coat removal')
path('M 1628,648 C 1634,713 1735,744 1783,678','#27383e',2.5,extra='marker-end="url(#arrow)"')
end()
text('hsc70-label',1668,769,'Auxilin + Hsc70',21,500,'middle')
text('atp-label',1668,802,'ATP-dependent uncoating',19,400,'middle')
for i,x in enumerate([480,988,1435]):arrow('progress-'+str(i),x,485,x+40,485)

# Live legend and explanatory text.
group('legend-cargo','Cargo legend');circle(80,855,13,'url(#cargo)','#a93e31',1.2);end()
text('legend-cargo-text',108,862,'Cargo',21)
receptor('legend-receptor',294,872,cargo=False)
text('legend-receptor-text',325,862,'Receptor',21)
adaptor('legend-ap2',530,852)
text('legend-ap2-text',558,862,'AP2',21)
triskelion('legend-clathrin',690,850,21)
text('legend-clathrin-text',728,862,'Clathrin',21)
group('legend-dynamin','Dynamin legend')
for y in [862,855,848]:add(f'<ellipse cx="916" cy="{y}" rx="24" ry="7" fill="none" stroke="url(#dynamin)" stroke-width="5"/>')
end();text('legend-dynamin-text',957,862,'Dynamin',21)
text('main-note',960,944,'Cargo stays in the lumen; coat assembly and removal occur on the cytosolic surface.',23,500,'middle')
text('scale-note',960,986,'Conceptual mammalian pathway; selected factors shown; not to scale. Assembly trajectories vary.',19,400,'middle','#607078')
add('</svg>')
(OUT/'endocytosis.svg').write_text('\n'.join(parts),encoding='utf-8',newline='\n')
print('Wrote endocytosis.svg with editable semantic objects and live labels.')
