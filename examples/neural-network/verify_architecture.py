"""Check the exported drawing's declared graph, actual endpoints and ReLU curve."""
from pathlib import Path
import xml.etree.ElementTree as ET
import re
import json
from collections import Counter

root=ET.parse(Path(__file__).with_name('neural-network.svg')).getroot()
ns={'s':'http://www.w3.org/2000/svg'}
units={n.get('id'):n for n in root.iter() if n.get('data-unit')}
counts=Counter(int(n.get('data-layer')) for n in units.values())
assert [counts[i] for i in range(4)]==[4,5,5,3]
expected={(a,b) for a,na in units.items() for b,nb in units.items() if int(nb.get('data-layer'))==int(na.get('data-layer'))+1}
edges=[n for n in root.iter() if n.get('data-connection')=='dense']
actual=[(n.get('data-source'),n.get('data-target')) for n in edges]
assert len(actual)==60 and len(set(actual))==60 and set(actual)==expected
for edge in edges:
    path=edge.find('s:path',ns)
    points=[float(v) for v in re.findall(r'-?\d+(?:\.\d+)?',path.get('d'))]
    assert len(points)==4
    ends=[]
    for attr in ['data-source','data-target']:
        circle=units[edge.get(attr)].find('s:circle',ns)
        ends.extend([float(circle.get('cx')),float(circle.get('cy'))])
    assert points==ends,edge.get('id')
relu=next(n for n in root.iter() if n.get('id')=='relu-function').find('s:path',ns).get('d')
assert relu=='M 2107,664 H 2148 L 2211,601'
assert 2211-2148==664-601 # unit positive slope with SVG's downward y axis
assert sum(n.get('id')=='softmax' for n in root.iter())==1
assert len([n for n in root.iter() if (n.get('id') or '').startswith('logit-to-softmax-')])==3
result={'graph_checks_passed':True,'layer_sizes':[4,5,5,3],'dense_edges':len(edges),'duplicate_or_missing_edges':0,'edge_geometry_matches_nodes':True,'relu_zero_and_unit_slope':True,'shared_softmax':True,'scope':'Exported conceptual graph and selected geometric properties, not a trained neural-network benchmark.'}
Path(__file__).with_name('architecture-check.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8',newline='\n')
print(json.dumps(result))
