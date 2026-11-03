"""Verify published file integrity and notebook provenance without executing cells."""
import hashlib
import json
from pathlib import Path

root = Path(__file__).resolve().parent
for line in (root / 'SHA256SUMS').read_text(encoding='utf-8').splitlines():
    expected, name = line.split('  ', 1)
    assert hashlib.sha256((root / name).read_bytes()).hexdigest() == expected, name
    print('OK', name)
for solution in json.loads((root / 'PROVENANCE.json').read_text(encoding='utf-8'))['solutions']:
    path = root / solution['file']
    assert hashlib.sha256(path.read_bytes()).hexdigest() == solution['sha256']
    notebook = json.loads(path.read_bytes())
    assert all(not c.get('outputs') for c in notebook['cells'])
    assert sum(c['cell_type'] == 'code' for c in notebook['cells']) == solution['code_cells_syntax_checked']
print('All release checks passed. Solver cells were not executed.')
