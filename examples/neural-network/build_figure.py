"""Original, editable 4-5-5-3 MLP; no raster assets or trained data."""
from pathlib import Path
from html import escape
import math
import json
import re

OUT=Path(__file__).resolve().parent
parts=[]
add=parts.append
INK='#23343c'; MUTED='#61717c'; TEAL='#167c83'; BLUE='#4a70b0'; PURPLE='#8064aa'; CORAL='#c96a58'; GOLD='#a86919'

def group(id,label='',**attrs):
    extra=' '.join(f'{k.replace("_","-")}="{escape(str(v),quote=True)}"' for k,v in attrs.items())
    add(f'<g id="{id}" data-editable="true" data-label="{escape(label or id)}" {extra}>')
def end(): add('</g>')
def text(id,x,y,label,size=26,fill=INK,anchor='start',weight=400,italic=False):
    sup=dict(zip('⁰¹²³⁴⁵⁶⁷⁸⁹ˡ⁻','0123456789l−'))
    subscript=dict(zip('₀₁₂₃₄₅₆₇₈₉ᵢⱼₖ','0123456789ijk'))
    chunks=re.findall(r'[⁰¹²³⁴⁵⁶⁷⁸⁹ˡ⁻]+|[₀₁₂₃₄₅₆₇₈₉ᵢⱼₖ]+|\[θ\]|[^⁰¹²³⁴⁵⁶⁷⁸⁹ˡ⁻₀₁₂₃₄₅₆₇₈₉ᵢⱼₖ\[]+',label)
    content=[];offset=0;previous_sup=''
    for chunk in chunks:
        is_sup=chunk[0] in sup;is_sub=chunk[0] in subscript or chunk=='[θ]'
        new_offset=-size*.38 if is_sup else size*.20 if is_sub else 0
        shown=''.join(sup.get(c,c) for c in chunk) if is_sup else ''.join(subscript.get(c,c) for c in chunk) if is_sub else chunk
        if chunk=='[θ]':shown='θ'
        dx=-size*.68*.59*len(previous_sup) if is_sub and previous_sup else 0
        content.append(f'<tspan dy="{new_offset-offset:g}" dx="{dx:g}" font-size="{size*.68 if is_sup or is_sub else size:g}">{escape(shown)}</tspan>')
        offset=new_offset;previous_sup=shown if is_sup else ''
    add(f'<text id="{id}" data-editable="true" x="{x}" y="{y}" font-size="{size}" fill="{fill}" text-anchor="{anchor}" font-weight="{weight}"'+(' font-style="italic"' if italic else '')+'>'+''.join(content)+'</text>')
def line(x1,y1,x2,y2,colour=INK,width=2,extra=''):
    add(f'<path d="M {x1:g},{y1:g} L {x2:g},{y2:g}" fill="none" stroke="{colour}" stroke-width="{width}" {extra}/>')
def arrow(id,points,colour=INK,width=2.5,dashed=False):
    group(id)
    d='M '+' L '.join(f'{x:g},{y:g}' for x,y in points)
    add(f'<path d="{d}" fill="none" stroke="{colour}" stroke-width="{width}" stroke-linejoin="round"'+(' stroke-dasharray="12 8"' if dashed else '')+'/>')
    x,y=points[-1];px,py=points[-2];angle=math.atan2(y-py,x-px);size=12
    pts=[(x,y),(x-size*math.cos(angle)+6*math.sin(angle),y-size*math.sin(angle)-6*math.cos(angle)),(x-size*math.cos(angle)-6*math.sin(angle),y-size*math.sin(angle)+6*math.cos(angle))]
    add('<polygon points="'+' '.join(f'{a:g},{b:g}' for a,b in pts)+f'" fill="{colour}"/>');end()
def box(id,x,y,w,h,fill='#ffffff',stroke='#cdd6dc',radius=16):
    group(id);add(f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{radius}" fill="{fill}" stroke="{stroke}" stroke-width="1.6"/>');end()
def node(id,x,y,r,gradient,stroke,label,**attrs):
    group(id,label,**attrs)
    add(f'<circle cx="{x}" cy="{y}" r="{r}" fill="url(#{gradient})" stroke="{stroke}" stroke-width="1.8"/>');end()
    text('label-'+id,x,y+10,label,30,INK,'middle',italic=True)

add('<?xml version="1.0" encoding="UTF-8"?>')
add('<svg xmlns="http://www.w3.org/2000/svg" width="2400" height="1400" viewBox="0 0 2400 1400" font-family="Georgia, Times New Roman, serif">')
add('<title>Feedforward neural network: a 4-5-5-3 multilayer perceptron</title><desc>Two ReLU hidden layers, three coupled softmax probabilities, a single hidden unit and a separate training workflow. Every adjacent-layer connection is explicitly drawn. All labels are live text.</desc>')
add('<defs>')
for name,light,dark in [('input','#f5fcfc','#b9d9dc'),('hidden1','#f5f8ff','#bdd0ed'),('hidden2','#faf7ff','#d2c6e6'),('logit','#fff8f5','#f0c3b7')]:
    add(f'<radialGradient id="{name}" cx="30%" cy="25%" r="85%"><stop offset="0" stop-color="{light}"/><stop offset="1" stop-color="{dark}"/></radialGradient>')
add('</defs><rect width="2400" height="1400" fill="#ffffff"/>')
text('title',1200,83,'Feedforward neural network',64,INK,'middle',700)
text('subtitle',1200,145,'Representation, prediction and gradient-based learning',33,MUTED,'middle',italic=True)
text('panel-a',70,245,'a',49,INK,weight=700)
text('panel-a-title',140,242,'Network architecture',35,INK,weight=700)
arrow('forward-flow',[(565,267),(1355,267)],TEAL,3.7)
text('forward-label',960,246,'Forward computation',29,TEAL,'middle',600)

xs=[155,545,975,1300]
ys=[[490,605,720,835],[450,560,670,780,890],[450,560,670,780,890],[550,670,790]]
layer_names=['Input','Hidden 1 · ReLU','Hidden 2 · ReLU','Logits']
layer_symbols=['x ∈ ℝ⁴','h¹ ∈ ℝ⁵','h² ∈ ℝ⁵','z ∈ ℝ³']
colours=[TEAL,BLUE,PURPLE,CORAL];grads=['input','hidden1','hidden2','logit']
sub='₁₂₃₄₅'
ids=[]
for l,(x,ys_l) in enumerate(zip(xs,ys)):
    ids.append([f'layer-{l}-unit-{i+1}' for i in range(len(ys_l))])
    text(f'layer-name-{l}',x,330,layer_names[l],30,colours[l],'middle',600)
    text(f'layer-symbol-{l}',x,376,layer_symbols[l],30,INK,'middle',italic=True)
for l in range(3):
    text(f'weight-shape-{l+1}',(xs[l]+xs[l+1])/2,405,['W¹: 5 × 4','W²: 5 × 5','W³: 3 × 5'][l],24,INK,'middle',italic=True)
    for i,y1 in enumerate(ys[l]):
        for j,y2 in enumerate(ys[l+1]):
            highlight=l==0 and j==2
            group(f'weight-{l+1}-{j+1}-{i+1}',f'W{l+1}[{j+1},{i+1}]',data_source=ids[l][i],data_target=ids[l+1][j],data_connection='dense')
            line(xs[l],y1,xs[l+1],y2,TEAL if highlight else ['#a0b9d9','#b6a6cc','#dba99e'][l],3.2 if highlight else 1.7)
            end()
for l,(x,ys_l) in enumerate(zip(xs,ys)):
    for i,y in enumerate(ys_l):
        label=(['x','h¹','h²','z'][l]+sub[i])
        node(ids[l][i],x,y,42,grads[l],colours[l],label,data_layer=l,data_unit=i+1)
# One coupled softmax operator, not independent scalar activations.
for i,y in enumerate(ys[-1]):
    arrow(f'logit-to-softmax-{i+1}',[(1342,y),(1435,635+i*35)],INK,2)
box('softmax',1435,611,145,118,'#fafbfc','#71808b',12)
text('softmax-label',1507,681,'Softmax',27,INK,'middle')
arrow('softmax-to-probability',[(1580,670),(1634,670)],INK,2.5)
text('probability-title-1',1642,520,'3-class',25,TEAL,'middle',600)
text('probability-title-2',1642,551,'probabilities',25,TEAL,'middle',600)
text('probability-space',1642,603,'p ∈ ℝ³',28,INK,'middle',italic=True)
group('probability-brackets')
add('<path d="M 1626,626 H 1618 V 754 H 1626 M 1673,626 H 1681 V 754 H 1673" fill="none" stroke="#23343c" stroke-width="2"/>');end()
for i,y in enumerate([651,693,735]):text(f'probability-{i+1}',1649,y,'p'+sub[i],28,INK,'middle',italic=True)
text('hidden-equation',865,967,'Hidden:  hˡ = ReLU(Wˡhˡ⁻¹ + bˡ),   l = 1, 2;   h⁰ = x',29,INK,'middle',italic=True)
text('output-equation',865,1015,'Output:  z = W³h² + b³;   p = softmax(z)',29,INK,'middle',italic=True)

# Single hidden unit. Its first three representative inputs are shown, with an ellipsis.
box('inset-frame',1740,228,600,804,'#ffffff','#c6cdd2',22)
text('panel-b',1774,286,'b',46,INK,weight=700)
text('panel-b-title',1838,282,'Inside one hidden unit',30,INK,weight=700)
text('inset-inputs-1',1820,356,'Previous-layer',23,BLUE,'middle')
text('inset-inputs-2',1820,386,'activations',23,BLUE,'middle')
for i,y in enumerate([454,574,694]):
    arrow(f'weighted-input-{i+1}',[(1852,y),(1980,589+i*20)],BLUE,2.2)
    text(f'weight-inset-label-{i+1}',1905,[497,564,660][i],'wⱼ'+sub[i],25,INK,'middle',italic=True)
    node(f'inset-input-{i+1}',1820,y,32,'hidden1',BLUE,'a'+sub[i])
text('inset-ellipsis',1820,753,'⋮',35,MUTED,'middle')
text('inset-other',1820,790,'other aᵢ',23,MUTED,'middle',italic=True)
node('sum',2010,610,35,'hidden2',PURPLE,'Σ')
text('bias-label',2010,367,'Bias',25,PURPLE,'middle')
text('bias-symbol',2010,411,'bⱼ',30,INK,'middle',italic=True)
arrow('bias-to-sum',[(2010,436),(2010,575)],PURPLE,2.4)
arrow('sum-to-relu',[(2045,610),(2090,610)],INK,2.5)
text('preactivation-symbol',2065,586,'zⱼ',27,INK,'middle',italic=True)
box('relu-frame',2090,535,138,153,'#fcfbfe','#89939a',9)
text('relu-label',2159,512,'ReLU',25,PURPLE,'middle')
arrow('relu-axis-x',[(2107,664),(2213,664)],MUTED,1.5)
arrow('relu-axis-y',[(2148,673),(2148,549)],MUTED,1.5)
group('relu-function','ReLU: max(0,z)',data_function='max(0,z)')
add(f'<path d="M 2107,664 H 2148 L 2211,601" fill="none" stroke="{PURPLE}" stroke-width="3.5"/>');end()
text('relu-zero',2141,683,'0',18,MUTED,'end')
text('relu-axis-label-x',2213,684,'z',18,MUTED,'middle',italic=True)
text('relu-axis-label-y',2137,556,'h',18,MUTED,'middle',italic=True)
arrow('relu-to-activation',[(2228,610),(2262,610)],INK,2.5)
node('inset-activation',2296,610,34,'hidden2',PURPLE,'hⱼ')
text('activation-label',2276,464,'Activation',23,PURPLE,'middle')
text('unit-affine-equation',2040,867,'zⱼ = Σᵢ wⱼᵢaᵢ + bⱼ',30,INK,'middle',italic=True)
text('unit-activation-equation',2040,916,'hⱼ = max(0, zⱼ)',30,INK,'middle',italic=True)
text('weight-definition',2040,980,'wⱼᵢ: weight from input i to hidden unit j',23,MUTED,'middle',italic=True)

# Training-only panel: backpropagation originates at the loss.
box('training-frame',60,1065,2280,262,'#fdfdfd','#c6cdd2',20)
text('panel-c',91,1124,'c',46,INK,weight=700)
text('panel-c-title',154,1120,'Training only',32,INK,weight=700)
text('prediction-label',883,1127,'Prediction',26,CORAL,'middle')
text('prediction-symbol',883,1198,'p',38,INK,'middle',italic=True)
arrow('prediction-to-loss',[(918,1190),(1085,1190)],INK,2.4)
text('target-label',1550,1127,'Target',26,TEAL,'middle')
text('target-symbol',1550,1198,'y',38,INK,'middle',italic=True)
arrow('target-to-loss',[(1512,1190),(1385,1190)],INK,2.4)
box('loss',1085,1125,300,110,'#ffffff','#73808a',12)
text('loss-label',1235,1168,'Cross-entropy loss',26,INK,'middle')
text('loss-equation',1235,1208,'L = −Σₖ yₖ log pₖ',27,INK,'middle',italic=True)
arrow('backpropagation',[(1235,1235),(1235,1290),(345,1290)],GOLD,3,True)
text('backprop-label',622,1174,'Backpropagation',28,GOLD,'middle',600)
text('backprop-detail',622,1210,'Gradients via the chain rule',25,GOLD,'middle')
text('backprop-note',622,1252,'Not an inference connection',22,MUTED,'middle',italic=True)
group('training-divider');line(1710,1110,1710,1290,'#cad2d8',1.5);end()
text('optimiser-label',2006,1143,'Gradient descent',28,INK,'middle',600)
text('optimiser-equation',2006,1200,'θ ← θ − η∇[θ]L',35,INK,'middle',italic=True)
text('optimiser-note',2006,1254,'Updates weights and biases',25,MUTED,'middle')
text('footer',1200,1375,'Illustrative 4–5–5–3 classifier. All adjacent-layer connections shown; biases in equations. Colours identify layers, not values.',24,MUTED,'middle')
add('</svg>')
(OUT/'neural-network.svg').write_text('\n'.join(parts)+'\n',encoding='utf-8',newline='\n')
(OUT/'architecture.json').write_text(json.dumps({'layer_sizes':[4,5,5,3],'hidden_activation':'ReLU','output_operator':'softmax','weight_shapes':[[5,4],[5,5],[3,5]],'bias_shapes':[5,5,3],'dense_connection_count':60,'data':'conceptual, no trained parameters'},indent=2)+'\n',encoding='utf-8',newline='\n')
print('Saved neural-network.svg and architecture.json')
