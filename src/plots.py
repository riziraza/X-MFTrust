from __future__ import annotations
from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt


def _save(fig, path):
    Path(path).parent.mkdir(parents=True, exist_ok=True)
    fig.tight_layout()
    fig.savefig(path, dpi=300, bbox_inches="tight")
    plt.close(fig)


def plot_main_results(root, out):
    df = pd.read_csv(Path(root)/"data/illustrative_results.csv")
    df = df[df.experiment == "main"]
    fig, ax = plt.subplots(figsize=(9,5))
    x = range(len(df))
    width = 0.18
    for i, col in enumerate(["precision","recall","map50","f1"]):
        ax.bar([v + (i-1.5)*width for v in x], df[col], width, label=col.upper())
    ax.set_xticks(list(x)); ax.set_xticklabels(df.method, rotation=15, ha="right")
    ax.set_ylim(0.65, 0.95); ax.set_ylabel("Score"); ax.set_title("Main Detection Performance")
    ax.legend(); _save(fig, out)


def plot_trust_ci(root, out):
    df = pd.read_csv(Path(root)/"data/trust_scores_ci.csv")
    fig, ax = plt.subplots(figsize=(8,5))
    ax.errorbar(df.condition, df["mean"], yerr=[df["mean"]-df["ci_low"], df["ci_high"]-df["mean"]], fmt="o-")
    ax.set_ylim(0.70, 1.00); ax.set_ylabel("Trust score"); ax.set_title("Trust Score Across Environmental Conditions")
    ax.tick_params(axis="x", rotation=20); _save(fig, out)


def plot_modality_contribution(root, out):
    df = pd.read_csv(Path(root)/"data/modality_contributions.csv").set_index("condition")
    fig, ax = plt.subplots(figsize=(9,5))
    bottom = None
    for col in ["RGB","Thermal","LiDAR","Environmental"]:
        ax.bar(df.index, df[col], bottom=bottom, label=col)
        bottom = df[col] if bottom is None else bottom + df[col]
    ax.set_ylim(0,1); ax.set_ylabel("Contribution")
    ax.set_title("Dynamic Modality Contribution")
    ax.legend(ncol=4); ax.tick_params(axis="x", rotation=20); _save(fig, out)


def plot_xai(root, out):
    df = pd.read_csv(Path(root)/"data/xai_comparison.csv")
    fig, ax = plt.subplots(figsize=(9,5))
    x = range(len(df)); ax.bar(x, df.faithfulness, label="Faithfulness")
    ax.plot(x, df.consistency, marker="o", label="Consistency")
    ax.set_xticks(list(x)); ax.set_xticklabels(df.method, rotation=15, ha="right")
    ax.set_ylim(0.6,0.9); ax.set_ylabel("Score"); ax.set_title("XAI Comparison")
    ax.legend(); _save(fig, out)


def plot_uncertainty_sensitivity(root, out):
    df = pd.read_csv(Path(root)/"data/uncertainty_sensitivity.csv")
    fig, ax = plt.subplots(figsize=(8,5))
    for col in ["Clear","Moderate_Fog","Severe_Fog"]:
        ax.plot(df.lambda_u, df[col], marker="o", label=col.replace("_"," "))
    ax.set_xlabel("Uncertainty weight $\\lambda_u$"); ax.set_ylabel("Trust score")
    ax.set_title("Uncertainty-Weight Sensitivity"); ax.legend(); _save(fig, out)


def plot_missing_modality(root, out):
    df = pd.read_csv(Path(root)/"data/illustrative_results.csv")
    df = df[df.experiment == "missing"]
    fig, ax = plt.subplots(figsize=(9,5))
    ax.plot(df.method, df.map50, marker="o", label="mAP")
    ax.plot(df.method, df.f1, marker="s", label="F1")
    ax.set_ylim(0.72,0.91); ax.set_ylabel("Score"); ax.set_title("Robustness to Missing/Corrupted Modalities")
    ax.tick_params(axis="x", rotation=20); ax.legend(); _save(fig, out)
