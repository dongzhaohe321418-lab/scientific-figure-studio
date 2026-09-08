"""Compose a contact sheet from the four original SVG documents (no raster tracing)."""
from pathlib import Path
import re
base=Path(__file__).parent
cases=['chemistry-sn2','earth-confined-aquifer','ecology-carbon','research-causal-dags']
parts=['<svg xmlns="http://www.w3.org/2000/svg" width="4000" height="2400" viewBox="0 0 4000 2400">','<rect width="4000" height="2400" fill="white"/>']
for i,s in enumerate(cases):
    source=(base/s/'figure.svg').read_text(encoding='utf-8')
    source=re.sub(r'<\?xml[^>]*>\s*','',source)
    source=re.sub(r'\bid="([^"]+)"',lambda m:f'id="case{i}-{m[1]}"',source)
    source=re.sub(r'url\(#([^)]+)\)',lambda m:f'url(#case{i}-{m[1]})',source)
    source=source.replace('<svg ',f'<svg x="{i%2*2000}" y="{i//2*1200}" ',1)
    parts.append(source)
parts.append('</svg>')
(base/'overview.svg').write_text('\n'.join(parts),encoding='utf-8',newline='\n')
