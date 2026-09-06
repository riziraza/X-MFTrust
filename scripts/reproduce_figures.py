from pathlib import Path
import sys
ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
from src.plots import *

if __name__ == "__main__":
    out = ROOT/"outputs/figures"; out.mkdir(parents=True, exist_ok=True)
    plot_main_results(ROOT, out/"main_results.png")
    plot_trust_ci(ROOT, out/"trust_scores_ci.png")
    plot_modality_contribution(ROOT, out/"modality_contributions.png")
    plot_xai(ROOT, out/"xai_comparison.png")
    plot_uncertainty_sensitivity(ROOT, out/"uncertainty_sensitivity.png")
    plot_missing_modality(ROOT, out/"missing_modality_robustness.png")
    print("Figures written to outputs/figures/")
