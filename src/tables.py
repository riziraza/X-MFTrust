from __future__ import annotations
from pathlib import Path
import pandas as pd


def load_data(root):
    root = Path(root)
    return {p.stem: pd.read_csv(p) for p in (root / "data").glob("*.csv")}


def save_markdown_table(df, path, index=False):
    Path(path).parent.mkdir(parents=True, exist_ok=True)
    Path(path).write_text(df.to_markdown(index=index), encoding="utf-8")


def save_latex_table(df, path, index=False, float_format="%.3f"):
    Path(path).parent.mkdir(parents=True, exist_ok=True)
    Path(path).write_text(df.to_latex(index=index, float_format=float_format), encoding="utf-8")


def make_summary_tables(root, output_dir):
    root, output_dir = Path(root), Path(output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)
    main = pd.read_csv(root / "data/illustrative_results.csv")
    hp = pd.read_csv(root / "data/hyperparameter_search.csv")
    ci = pd.read_csv(root / "data/trust_scores_ci.csv")
    mod = pd.read_csv(root / "data/modality_contributions.csv")
    xai = pd.read_csv(root / "data/xai_comparison.csv")
    unc = pd.read_csv(root / "data/uncertainty_sensitivity.csv")

    tables = {
        "main_results": main[main.experiment == "main"].drop(columns=["experiment", "trust"]),
        "missing_modality": main[main.experiment == "missing"].drop(columns=["experiment"]),
        "unseen_severe_fog": main[main.experiment == "unseen_severe_fog"].drop(columns=["experiment", "trust"]),
        "hyperparameters": hp,
        "trust_ci": ci,
        "modality_contributions": mod,
        "xai_comparison": xai,
        "uncertainty_sensitivity": unc,
    }
    for name, df in tables.items():
        save_markdown_table(df, output_dir / f"{name}.md")
        save_latex_table(df, output_dir / f"{name}.tex")
