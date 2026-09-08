"""Rebuild the four original semantic SVG examples, without repeating image generation."""
from pathlib import Path
import math,random
from vector import Figure,INK,TEAL,CORAL,GOLD,PURPLE,MUTED

BASE=Path(__file__).parent

def chemistry():
 f=Figure('SN2 nucleophilic substitution');f.header('SN2 nucleophilic substitution','One concerted step · explicit atom, charge and electron-pair accounting')
 f.box('mechanism-frame',55,175,1890,545,'white','#b8cfd0',20)
 f.text('panel-a',85,228,'a',43,TEAL,weight=700);f.text('panel-a-title',145,225,'A concerted substitution',34,TEAL,weight=700)
 # Reactants: hydroxide plus methyl bromide.
 for id,a,b in [('r-oh',(100,430),(185,430)),('r-cbr',(430,430),(555,430)),('r-ch1',(430,430),(413,320)),('r-ch2',(430,430),(365,510)),('r-ch3',(430,430),(495,510))]:f.bond(id,*a,*b)
 for id,x,y,e in [('r-oh-h',100,430,'H'),('r-o',185,430,'O'),('r-c',430,430,'C'),('r-br',555,430,'Br'),('r-h1',413,320,'H'),('r-h2',365,510,'H'),('r-h3',495,510,'H')]:f.atom(id,x,y,e,'reactant')
 f.text('r-minus',225,397,'−',30,INK,'middle');f.text('r-plus',295,441,'+',38,INK,'middle')
 f.text('reactants-label',330,620,'HO⁻ + CH₃Br',31,INK,'middle')
 f.arrow('step-to-ts','M640,430 L730,430',(730,430),(640,430),INK,3)
 # Equatorial plane is conceptual; two axial bonds remain partial.
 f.group('equatorial-plane');f.ellipse(1000,430,89,148,'#e9e2f0',extra='fill-opacity="0.65"');f.end()
 for id,a,b,p in [('t-oh',(800,430),(875,430),False),('t-form',(875,430),(1000,430),True),('t-break',(1000,430),(1165,430),True),('t-ch1',(1000,430),(1000,300),False),('t-ch2',(1000,430),(929,520),False),('t-ch3',(1000,430),(1071,520),False)]:f.bond(id,*a,*b,p)
 for id,x,y,e in [('t-oh-h',800,430,'H'),('t-o',875,430,'O'),('t-c',1000,430,'C'),('t-br',1165,430,'Br'),('t-h1',1000,300,'H'),('t-h2',929,520,'H'),('t-h3',1071,520,'H')]:f.atom(id,x,y,e,'transition')
 f.group('ts-brackets');f.path('M785,260 H765 V590 H785 M1210,260 H1230 V590 H1210','none',INK,2.4);f.end()
 f.text('ts-charge',1255,273,'‡⁻',34);f.text('t-form-label',892,573,'Bond forming',24,TEAL,'middle');f.text('t-break-label',1135,573,'Bond breaking',24,PURPLE,'middle')
 f.text('ts-label',1000,650,'One transition state; no intermediate',29,INK,'middle')
 f.arrow('step-to-product','M1295,430 L1390,430',(1390,430),(1295,430),INK,3)
 for id,a,b in [('p-co',(1530,430),(1650,430)),('p-oh',(1650,430),(1740,493)),('p-ch1',(1530,430),(1515,320)),('p-ch2',(1530,430),(1463,510)),('p-ch3',(1530,430),(1595,510))]:f.bond(id,*a,*b)
 for id,x,y,e in [('p-c',1530,430,'C'),('p-o',1650,430,'O'),('p-oh-h',1740,493,'H'),('p-h1',1515,320,'H'),('p-h2',1463,510,'H'),('p-h3',1595,510,'H'),('p-br',1865,430,'Br')]:f.atom(id,x,y,e,'product')
 f.text('p-plus',1772,441,'+',36,INK,'middle');f.text('p-minus',1911,400,'−',30,INK,'middle');f.text('products-label',1640,620,'CH₃OH + Br⁻',31,INK,'middle')
 f.box('electron-frame',55,755,1890,332,'white','#c9c0d4',20)
 f.text('panel-b',85,810,'b',43,PURPLE,weight=700);f.text('panel-b-title',145,808,'Electron-pair movement',34,PURPLE,weight=700)
 f.text('e-h',160,975,'H',43,INK,'middle');f.text('e-o',270,975,'O⁻',43,CORAL,'middle');f.text('e-plus',388,975,'+',39,INK,'middle')
 f.text('e-c',550,975,'CH₃',43,INK,'middle');f.text('e-br',728,975,'Br',43,PURPLE,'middle')
 f.group('e-oh-bond');f.path('M183,960 H240','none',INK,3);f.end()
 f.group('e-cbr-bond');f.path('M602,960 H690','none',INK,3);f.end()
 f.group('oxygen-pair');f.ellipse(267,923,3.8,3.8,CORAL);f.ellipse(281,923,3.8,3.8,CORAL);f.end()
 f.arrow('electron-attack','M274,923 C348,830 454,845 520,929',(520,929),(454,845),CORAL,3.5,data_origin='oxygen-lone-pair',data_destination='carbon',data_species='electron-pair')
 f.arrow('electron-departure','M646,960 C655,862 714,862 728,928',(728,928),(714,862),PURPLE,3.5,data_origin='C-Br-bond',data_destination='bromine',data_species='electron-pair')
 f.text('selected-pair-note',472,1040,'Selected reacting lone pair shown; other lone pairs omitted.',24,MUTED,'middle')
 f.text('rate-equation',1390,913,'rate = k[CH₃Br][HO⁻]',37,INK,'middle',italic=True)
 f.text('rate-note',1390,969,'Bimolecular rate law',27,PURPLE,'middle');f.text('balance-note',1390,1022,'Atoms conserved · net charge −1 on both sides',26,TEAL,'middle')
 f.text('footer',1000,1148,'Conceptual methyl substitution; not a chiral example. Molecular projection is schematic; no quantitative energetics implied.',24,MUTED,'middle')
 f.save(BASE/'chemistry-sn2')

def aquifer():
 f=Figure('Confined aquifer and artesian head',True);f.header('Confined aquifer and artesian head','A static standpipe measurement in a conceptual geological section')
 ground='M100,265 C220,270 290,296 365,323 C700,454 1240,530 1880,550'
 top='M100,265 C260,279 350,319 520,422 C880,628 1280,655 1880,665'
 bottom='M100,435 C300,449 405,498 570,585 C920,748 1300,788 1880,795'
 upper=ground+' L1880,665 C1280,655 880,628 520,422 C350,319 260,279 100,265 Z'
 lower=bottom+' L1880,945 L100,945 Z'
 bed=top+' L1880,795 C1300,788 920,748 570,585 C405,498 300,449 100,435 Z'
 f.group('lower-aquitard');f.path(lower,'#af9b7c','#8a795f',2);f.end()
 f.group('upper-aquitard');f.path(upper,'#d8c9ae','#9b8e77',2);f.end()
 f.group('aquifer',data_pool='saturated-aquifer');f.path(bed,'url(#blue)','#6e9cb3',2);f.end()
 f.add(f'<defs><clipPath id="bed-clip"><path d="{bed}"/></clipPath><clipPath id="lower-clip"><path d="{lower}"/></clipPath></defs>')
 rng=random.Random(14)
 f.group('aquifer-grains');f.add('<g clip-path="url(#bed-clip)">')
 for i in range(600):
  x=rng.uniform(110,1870);y=rng.uniform(270,795);f.ellipse(round(x,1),round(y,1),rng.uniform(2,5),rng.uniform(1,3),'#edf5f7','#769db1',.5)
 f.end();f.end()
 f.group('lower-bedding');f.add('<g clip-path="url(#lower-clip)">')
 for j in range(10):f.path(f'M70,{440+j*48} C600,{610+j*35} 1160,{780+j*20} 1900,{800+j*16}','none','#8c7b62',1)
 f.end();f.end()
 f.group('land-surface');f.path(ground,'none','#668056',6);f.end()
 for i,(x,y) in enumerate([(180,272),(245,285),(315,309)]):f.arrow(f'recharge-{i}',f'M{x},{y-95} L{x},{y-7}',(x,y-7),(x,y-95),'#397f9f',3)
 f.text('recharge-label',245,169,'Recharge at outcrop',29,TEAL,'middle',600)
 for i,(x,y,x2,y2) in enumerate([(320,399,465,466),(640,556,810,629),(1000,682,1180,706),(1260,716,1385,722)]):f.arrow(f'flow-{i}',f'M{x},{y} L{x2},{y2}',(x2,y2),(x,y),'#397f9f',4,data_source='recharge',data_destination='aquifer',data_species='groundwater')
 f.group('standpipe',data_roof_y=649,data_floor_y=787,data_rim_y=205,data_water_y=345,data_ground_y=542,data_screen_top=685,data_screen_bottom=755)
 f.rect(1450,205,36,565,'#edf1f2','#788892',4);f.rect(1457,345,22,415,'#72b9d4','none',0)
 f.ellipse(1468,205,18,5,'#f8fafb','#788892',1.8)
 f.path('M1457,345 H1479','none','#276d94',2.5)
 for y in range(685,756,10):f.path(f'M1451,{y} H1485','none','#455f72',1.5)
 f.end()
 f.group('static-head-line');f.path('M1325,345 H1770','none','#315f8e',2.8,'stroke-dasharray="12 9"');f.end()
 f.text('static-head-label',1645,320,'Static head',28,'#315f8e','middle',600)
 f.text('standpipe-label',1590,451,'Cased standpipe',27,INK)
 f.arrow('standpipe-callout','M1570,459 L1488,470',(1488,470),(1570,459),MUTED,1.5)
 f.text('upper-label',1150,552,'Upper aquitard · low permeability',29,INK,'middle')
 f.text('aquifer-label',945,653,'Confined aquifer · saturated',29,'#245a73','middle',600)
 f.text('lower-label',1050,883,'Lower aquitard',30,INK,'middle')
 f.text('screen-label',1550,749,'Screen only in aquifer',26,INK)
 f.arrow('screen-callout','M1530,742 L1487,730',(1487,730),(1530,742),MUTED,1.5)
 f.box('interpretation',180,985,1640,122,'#f8fafb','#cbd5d8',18)
 f.text('interpretation-title',1000,1027,'Static measurement shown: the pipe rim is above its water level.',28,INK,'middle',600)
 f.text('interpretation-detail',1000,1070,'A separate outlet below available head may flow; discharge changes the local head.',27,MUTED,'middle')
 f.text('footer',1000,1154,'Conceptual section; local head marker only. Geometry and vertical exaggeration are illustrative; no field measurements implied.',24,MUTED,'middle')
 f.save(BASE/'earth-confined-aquifer')

def leaf(f,id,x,y,scale=1,angle=0):
 f.group(id);f.add(f'<g transform="translate({x} {y}) rotate({angle}) scale({scale})">')
 f.path('M0,0 C-52,-30 -65,-97 0,-135 C65,-97 52,-30 0,0 Z','url(#leaf)','#507354',1.5)
 f.path('M0,0 Q4,-62 0,-127','none','#e2deb0',1.4)
 for k in range(1,5):f.path(f'M1,{-k*23} L{-32+k*2},{-k*23-16} M1,{-k*23} L{32-k*2},{-k*23-16}','none','#d3d3a0',.9)
 f.end();f.end()

def carbon():
 f=Figure('Carbon pathways in a terrestrial ecosystem');f.header('Carbon pathways in a terrestrial ecosystem')
 f.box('atmosphere',620,155,880,95,'url(#teal)',TEAL,38);f.text('atmosphere-label',1060,216,'Atmospheric CO₂',38,INK,'middle',700)
 f.group('soil-block',data_pool='soil');f.path('M110,680 L1760,680 L1880,730 L1880,1050 L1800,1100 L110,1060 Z','url(#soil)','#6b593e',2);f.path('M1760,680 L1880,730 L1880,1050 L1760,1020 Z','#887354','#69593f',1.4);f.end()
 f.add('<defs><clipPath id="soil-clip"><path d="M112,685 H1756 V1070 L112,1057 Z"/></clipPath></defs>')
 f.group('soil-grains');f.add('<g clip-path="url(#soil-clip)">');rng=random.Random(24)
 for i in range(280):f.ellipse(round(rng.uniform(115,1760),1),round(rng.uniform(688,1070),1),rng.uniform(1,5),rng.uniform(1,3),['#baa076','#6b563d','#d0b88d'][i%3])
 f.end();f.end()
 # Branching roots stay in the soil.
 f.group('roots');f.add('<g clip-path="url(#soil-clip)">')
 for j in range(7):
  x=325+j*38;f.path(f'M{x},670 C{x+12},740 {x-20},831 {x-70},955','none','#dfc8a0',2.5)
  for k in range(3):f.path(f'M{x-5-k*12},{760+k*50} Q{x+28},{790+k*45} {x+70},{825+k*50}','none','#d5bc91',1.6)
 f.end();f.end()
 # Original vector plants with individually editable leaves and veins.
 f.group('plant-stems',data_pool='plants')
 for x,y in [(390,415),(500,350),(590,472)]:f.path(f'M{x},689 Q{x-40},530 {x}, {y}','none','#72835b',8)
 f.end()
 for i,(x,y,s,a) in enumerate([(392,544,.85,-58),(411,508,.75,50),(495,461,.8,-54),(504,395,.66,42),(485,560,.75,58),(572,573,.7,-50),(586,510,.65,38),(380,630,.76,-67),(545,630,.74,70),(637,636,.63,52),(430,656,.62,-35)]):leaf(f,f'leaf-{i}',x,y,s,a)
 # Generic herbivore silhouette, not a claim of species morphology.
 f.group('herbivore',data_pool='herbivore')
 f.ellipse(1410,572,125,101,'url(#fur)','#8c7965',2);f.ellipse(1294,607,67,56,'url(#fur)','#8c7965',2)
 f.ellipse(1284,503,20,91,'url(#fur)','#8c7965',2,extra='transform="rotate(-14 1284 503)"');f.ellipse(1319,507,19,94,'url(#fur)','#8c7965',2,extra='transform="rotate(8 1319 507)"')
 f.ellipse(1284,506,8,68,'#b8978a');f.ellipse(1319,510,7,69,'#b8978a');f.ellipse(1497,605,34,34,'#ece6d9','#a29482',1)
 f.ellipse(1384,658,76,22,'url(#fur)','#8c7965',1.6);f.ellipse(1286,658,47,15,'url(#fur)','#8c7965',1.6)
 f.ellipse(1276,600,9,10,INK);f.ellipse(1273,597,2,2,'white');f.ellipse(1238,621,8,5,'#745647')
 for j in range(70):
  x=1326+rng.random()*156;y=522+rng.random()*90;f.path(f'M{x:.1f},{y:.1f} l8,-5','none','#bdad94',1.1)
 f.end()
 f.box('plant-label-box',240,627,420,60,'#fffffa','#617b59',18);f.text('plant-label',450,666,'Plant biomass',29,INK,'middle',600)
 f.box('animal-label-box',1280,667,380,55,'#fffffa','#617b59',18);f.text('animal-label',1470,703,'Herbivore biomass',28,INK,'middle',600)
 f.box('soil-pool-box',500,878,470,94,'#fcf0d4','#6f5c3e',20);f.text('soil-pool-label',735,937,'Soil organic matter',30,'#4b3a25','middle',600)
 f.group('microbes',data_pool='microbes');f.ellipse(1500,931,177,163,'#f7f5e6','#376f6c',3)
 for i in range(15):
  a=i*2.399;r=30+85*((i%5)/5);x=1500+math.cos(a)*r;y=914+math.sin(a)*r
  f.ellipse(round(x,1),round(y,1),12+(i%3)*3,7,'#8daf9b','#5b8574',1.5,extra=f'transform="rotate({i*27} {x:.1f} {y:.1f})"')
  f.path(f'M{x:.1f},{y:.1f} q-20,-25 -35,-14','none','#92a887',1)
 f.end();f.text('microbial-label',1500,1021,'Microbial biomass',27,INK,'middle',600)
 # Nine explicitly sourced carbon transfers. Shape positions are conceptual only.
 transfers=[
 ('photosynthesis','atmosphere','plants','M620,201 H430 Q355,201 355,287 V360 Q355,440 392,510',(392,510),(355,440),TEAL),
 ('plant-respiration','plants','atmosphere','M646,426 C718,347 705,292 722,252',(722,252),(705,292),TEAL),
 ('herbivory','plants','herbivore','M680,550 C852,520 1038,520 1198,557',(1198,557),(1038,520),TEAL),
 ('animal-respiration','herbivore','atmosphere','M1428,456 C1510,342 1415,316 1390,253',(1390,253),(1415,316),TEAL),
 ('litter','plants','soil','M535,690 C540,758 561,800 618,866',(618,866),(561,800),'#fff9e9'),
 ('waste','herbivore','soil','M1270,722 C1130,770 1030,790 910,877',(910,877),(1030,790),'#fff9e9'),
 ('decomposition','soil','microbes','M979,914 H1311',(1311,914),(979,914),'#fff9e9'),
 ('microbial-respiration','microbes','atmosphere','M1658,841 C1770,695 1750,440 1750,288 Q1750,201 1510,201',(1510,201),(1640,201),TEAL),
 ('residues','microbes','soil','M1322,987 Q1152,1040 982,967',(982,967),(1152,1040),'#fff9e9')]
 for id,src,dst,d,tip,prev,col in transfers:f.arrow(id,d,tip,prev,col,4,data_source=src,data_destination=dst,data_species='carbon')
 labels=[('photosynthesis-label',490,304,'Photosynthesis',TEAL),('plant-resp-label',800,359,'Plant respiration',TEAL),('herbivory-label',910,503,'Herbivory',TEAL),('animal-resp-label',1285,335,'Animal respiration',TEAL),('litter-label',701,797,'Litter + dead roots','#fff7e7'),('waste-label',1050,751,'Waste + remains','#fff7e7'),('decomp-label',1142,858,'Decomposition','#fff7e7'),('decomp-label-2',1142,892,'+ uptake','#fff7e7'),('residues-label',1128,1050,'Microbial residues','#fff7e7'),('microbial-resp-label',1640,400,'Microbial',TEAL),('microbial-resp-label-2',1640,434,'respiration',TEAL)]
 for id,x,y,s,col in labels:f.text(id,x,y,s,26,col,'middle',600)
 f.arrow('light-energy','M170,335 C175,405 230,460 297,497',(297,497),(230,460),GOLD,3,True,data_species='energy',data_source='sun',data_destination='plants')
 f.text('light-label',168,289,'Light energy',26,GOLD,'middle',600)
 f.text('magnification-label',1500,1118,'Microbes magnified schematically',22,MUTED,'middle')
 f.text('footer',1000,1172,'Selected terrestrial pathways; not a complete carbon budget or steady-state model. No rates or pool sizes are implied.',24,MUTED,'middle')
 f.save(BASE/'ecology-carbon')

def causal():
 f=Figure('Confounding, mediation and collider bias',True);f.header('Confounding, mediation and collider bias')
 configs=[('confounder',60,'a','Confounder',{'Z':(350,400),'X':(165,600),'Y':(535,600)},[('Z','X'),('Z','Y'),('X','Y')]),('mediator',705,'b','Mediator',{'X':(815,600),'M':(995,400),'Y':(1180,600)},[('X','M'),('M','Y'),('X','Y')]),('collider',1350,'c','Collider',{'X':(1460,390),'Y':(1825,390),'C':(1642,610)},[('X','C'),('Y','C')])]
 for slug,x,letter,title,nodes,edges in configs:
  f.box(slug+'-panel',x,190,590,770,'white','#c4cfd6',18);f.text(slug+'-letter',x+33,252,letter,44,INK,weight=700);f.text(slug+'-title',x+295,252,title,37,INK,'middle',700)
  for a,b in edges:
   xa,ya=nodes[a];xb,yb=nodes[b];ang=math.atan2(yb-ya,xb-xa);sx=xa+61*math.cos(ang);sy=ya+61*math.sin(ang);tx=xb-64*math.cos(ang);ty=yb-64*math.sin(ang)
   d=f'M{sx:g},{sy:g} L{tx:g},{ty:g}';previous=(sx,sy)
   if slug=='mediator' and a=='X' and b=='Y':sx,sy=nodes[a][0]+54,nodes[a][1]+28;tx,ty=nodes[b][0]-54,nodes[b][1]+28;d=f'M{sx},{sy} Q995,757 {tx},{ty}';previous=(995,757)
   col=GOLD if slug=='confounder' and a=='Z' else CORAL if slug=='collider' else TEAL
   f.arrow(slug+'-'+a+'-'+b,d,(tx,ty),previous,col,4,data_source=a,data_destination=b,data_graph=slug,data_species='causal-assumption')
  for name,(nx,ny) in nodes.items():
   special=name in 'ZMC';gradient={'Z':'amber','M':'teal','C':'coral'}.get(name,'blue')
   f.group(slug+'-node-'+name,data_graph=slug,data_node=name);f.ellipse(nx,ny,59,59,'url(#'+gradient+')',{'Z':GOLD,'M':TEAL,'C':CORAL}.get(name,'#58758e'),2);f.end();f.text(slug+'-symbol-'+name,nx,ny+18,name,58,INK,'middle',600)
  f.group(slug+'-rule');f.path(f'M{x+25},742 H{x+565}','none','#c2ccd3',1.7);f.end()
 f.text('confounder-note',350,319,'Pre-exposure common cause',27,INK,'middle',italic=True)
 f.text('confounder-line1',355,803,'Conditioning on Z blocks',28,INK,'middle');f.text('confounder-line2',355,848,'the backdoor path X ← Z → Y.',28,INK,'middle')
 f.text('mediator-note',1000,319,'On a causal pathway',27,INK,'middle',italic=True)
 for i,s in enumerate(['For the total effect, do not adjust','away the mediated pathway.','Statement applies to the graph shown.']):f.text(f'mediator-line-{i}',1000,803+i*45,s,27 if i<2 else 23,INK if i<2 else MUTED,'middle',italic=i==2)
 f.group('condition-collider',data_condition='C');f.ellipse(1642,610,73,73,'none',CORAL,2.5,'stroke-dasharray="12 10"');f.end()
 f.text('collider-note',1642,711,'Common effect',26,INK,'middle',italic=True)
 for i,s in enumerate(['Without conditioning: path blocked.','Conditioning on C can open','a noncausal association.']):f.text(f'collider-line-{i}',1645,803+i*45,s,27,INK,'middle')
 f.group('condition-legend');f.ellipse(1530,1008,17,17,'none',CORAL,2.3,'stroke-dasharray="7 6"');f.end();f.text('condition-legend-text',1565,1017,'Dashed outline: conditioning',25,INK)
 f.text('xy-legend',460,1017,'X: exposure   ·   Y: outcome',27,INK,'middle')
 f.text('principle',1000,1080,'Draw causal assumptions before selecting adjustment variables.',31,INK,'middle',600)
 f.text('footer-1',1000,1132,'Arrows encode assumed direct causal relations. A graph does not establish an empirical effect or a complete identification strategy.',24,MUTED,'middle')
 f.text('footer-2',1000,1170,'Illustrative DAGs; statements apply to the depicted paths and assumptions. Conditioning does not create a causal arrow.',24,MUTED,'middle')
 f.save(BASE/'research-causal-dags')

if __name__=='__main__':
 for fn in [chemistry,aquifer,carbon,causal]:fn()
 print('Rebuilt four editable SVGs.')
