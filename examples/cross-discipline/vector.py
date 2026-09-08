"""Small original SVG drawing helpers for the cross-discipline live evaluation."""
from html import escape
from pathlib import Path
import math
import re

INK='#223842';TEAL='#197780';CORAL='#c86958';GOLD='#ad7b31';PURPLE='#7b5b91';MUTED='#61727b'
class Figure:
 def __init__(self,title,serif=False):
  self.p=['<?xml version="1.0" encoding="UTF-8"?>',f'<svg xmlns="http://www.w3.org/2000/svg" width="2000" height="1200" viewBox="0 0 2000 1200" font-family="{("Georgia, Times New Roman, serif" if serif else "Arial, Helvetica, sans-serif")}">',f'<title>{escape(title)}</title><desc>Original conceptual scientific diagram with live labels and separate editable components. See caption and sources.</desc>','<rect width="2000" height="1200" fill="white"/>','<defs>']
  for name,light,dark in [('blue','#f1f8fc','#a4c6dc'),('teal','#edfafa','#94c8c5'),('purple','#f8f2fa','#b9a4c9'),('amber','#fff5dc','#d7b571'),('coral','#fff1e9','#e8afa0'),('carbon','#90989a','#20272b'),('oxygen','#ffded2','#db705a'),('bromine','#d0a0bb','#663d69'),('hydrogen','#ffffff','#c1c8cd'),('leaf','#b8cd80','#3c7556'),('soil','#a38b63','#6d573d'),('fur','#dbcebb','#95816c')]:
   self.p.append(f'<radialGradient id="{name}" cx="30%" cy="25%" r="85%"><stop offset="0" stop-color="{light}"/><stop offset="1" stop-color="{dark}"/></radialGradient>')
  self.p.append('</defs>')
 def add(self,s):self.p.append(s)
 def group(self,id,label='',**attrs):
  extra=' '.join(f'{k.replace("_","-")}="{escape(str(v),quote=True)}"' for k,v in attrs.items())
  self.add(f'<g id="{id}" data-editable="true" data-label="{escape(label or id)}" {extra}>')
 def end(self):self.add('</g>')
 def text(self,id,x,y,s,size=28,fill=INK,anchor='start',weight=400,italic=False):
  sup=dict(zip('⁰¹²³⁴⁵⁶⁷⁸⁹⁻⁺','0123456789−+'));sub=dict(zip('₀₁₂₃₄₅₆₇₈₉ᵢⱼₖ','0123456789ijk'))
  chunks=re.findall(r'[⁰¹²³⁴⁵⁶⁷⁸⁹⁻⁺]+|[₀₁₂₃₄₅₆₇₈₉ᵢⱼₖ]+|[^⁰¹²³⁴⁵⁶⁷⁸⁹⁻⁺₀₁₂₃₄₅₆₇₈₉ᵢⱼₖ]+',s)
  content=[];offset=0
  for c in chunks:
   table=sup if c[0] in sup else sub if c[0] in sub else {}
   new=-size*.38 if table is sup else size*.2 if table is sub else 0
   content.append(f'<tspan dy="{new-offset:g}" font-size="{size*.7 if table else size:g}">{escape("".join(table.get(v,v) for v in c))}</tspan>');offset=new
  self.add(f'<text id="{id}" data-editable="true" x="{x}" y="{y}" font-size="{size}" fill="{fill}" text-anchor="{anchor}" font-weight="{weight}"'+(' font-style="italic"' if italic else '')+'>'+''.join(content)+'</text>')
 def path(self,d,fill='none',stroke=INK,width=2,extra=''):
  self.add(f'<path d="{d}" fill="{fill}" stroke="{stroke}" stroke-width="{width}" stroke-linejoin="round" stroke-linecap="round" {extra}/>')
 def ellipse(self,x,y,rx,ry,fill,stroke='none',width=1,extra=''):
  self.add(f'<ellipse cx="{x}" cy="{y}" rx="{rx}" ry="{ry}" fill="{fill}" stroke="{stroke}" stroke-width="{width}" {extra}/>')
 def rect(self,x,y,w,h,fill='white',stroke='#c9d3d7',radius=12):
  self.add(f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{radius}" fill="{fill}" stroke="{stroke}" stroke-width="1.8"/>')
 def box(self,id,x,y,w,h,fill='white',stroke='#c9d3d7',radius=12):
  self.group(id);self.rect(x,y,w,h,fill,stroke,radius);self.end()
 def arrow(self,id,d,tip,previous,colour=TEAL,width=4,dashed=False,**attrs):
  self.group(id,**attrs);self.path(d,'none',colour,width,'stroke-dasharray="12 9"' if dashed else '')
  x,y=tip;px,py=previous;a=math.atan2(y-py,x-px);r=15;half=7
  q=[(x,y),(x-r*math.cos(a)+half*math.sin(a),y-r*math.sin(a)-half*math.cos(a)),(x-r*math.cos(a)-half*math.sin(a),y-r*math.sin(a)+half*math.cos(a))]
  self.add('<polygon data-arrowhead="true" points="'+' '.join(f'{i:g},{j:g}' for i,j in q)+f'" fill="{colour}"/>');self.end()
 def atom(self,id,x,y,element,state):
  gradient={'C':'carbon','H':'hydrogen','O':'oxygen','Br':'bromine'}[element];r={'C':33,'H':23,'O':33,'Br':38}[element]
  self.group(id,element,data_element=element,data_state=state);self.ellipse(x,y,r,r,'url(#'+gradient+')','#879199',1);self.end()
  self.text(id+'-label',x,y+10,element,29,'#ffffff' if element in ['C','Br'] else INK,'middle',600)
 def bond(self,id,x1,y1,x2,y2,partial=False):
  self.group(id,data_bond='partial' if partial else 'single');self.path(f'M{x1},{y1} L{x2},{y2}','none','#7d8485',4,'stroke-dasharray="10 9"' if partial else '');self.end()
 def header(self,title,subtitle=''):
  self.text('figure-title',1000,83,title,52,INK,'middle',700)
  if subtitle:self.text('figure-subtitle',1000,133,subtitle,27,MUTED,'middle')
 def save(self,folder):
  folder=Path(folder);folder.mkdir(exist_ok=True,parents=True)
  (folder/'figure.svg').write_text('\n'.join(self.p+['</svg>'])+'\n',encoding='utf-8',newline='\n')
