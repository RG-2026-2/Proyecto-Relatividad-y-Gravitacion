import json
from pathlib import Path
path = Path(r'c:\Users\Equipo Hogar\Desktop\Relatividad General\Proyecto-Relatividad-y-Gravitacion\Proyecto.ipynb')
nb = json.loads(path.read_text(encoding='utf-8'))
old = 'fig.add_trace(go.Scattergl('
new = 'fig.add_trace(go.Scatter3d('
updated = False
for cell in nb['cells']:
    if cell['cell_type'] == 'code':
        src = ''.join(cell['source'])
        if 'graficar_trayectorias_disco_plotly' in src:
            src = src.replace(old, new)
            src = src.replace('yaxis_scaleanchor="x"', 'scene=dict(\n            xaxis_title="x [m]",\n            yaxis_title="y [m]",\n            zaxis_title="z [m]",\n            aspectmode="data"\n        )')
            cell['source'] = [src]
            updated = True
            break
if not updated:
    raise RuntimeError('target cell not found')
path.write_text(json.dumps(nb, ensure_ascii=False, indent=1), encoding='utf-8')
print('patched')
