from pathlib import Path
import argparse, json, sys
ROOT=Path(__file__).resolve().parents[1]; sys.path.insert(0,str(ROOT))
from src.visualization import make_severe_fog_grid

if __name__ == "__main__":
    ap=argparse.ArgumentParser()
    ap.add_argument("--manifest",required=True,help="JSON list of qualitative examples")
    ap.add_argument("--output",default="outputs/figures/severe_fog_results.png")
    a=ap.parse_args()
    rows=json.loads(Path(a.manifest).read_text())
    make_severe_fog_grid(rows,a.output)
    print(a.output)
