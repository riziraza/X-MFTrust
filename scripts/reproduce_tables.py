from pathlib import Path
import sys
ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
from src.tables import make_summary_tables

if __name__ == "__main__":
    make_summary_tables(ROOT, ROOT/"outputs/tables")
    print("Tables written to outputs/tables/")
