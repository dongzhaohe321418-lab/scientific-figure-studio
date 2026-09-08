"""Run the recorded examples' deterministic mutation suite; no model calls."""
import sys
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT/'examples'/'cross-discipline'))
from test_cases import CaseChecks
