# X-MFTrust Reproducibility Repository

This repository contains the reproducibility code and result tables corresponding to the X-MFTrust manuscript:

**X-MFTrust: An Explainable Multi-Modal Fusion Framework for Trustworthy UAV-Based Object Detection in Foggy and Hazy Environments**

## Important reproducibility note

The numerical values included in `data/illustrative_results.csv` reproduce the **illustrative/simulated/estimated values prepared during the manuscript-revision drafting process**. They are included so that the tables and analytical plots can be regenerated consistently. They must **not** be presented as newly measured experimental results unless they are verified against the actual experimental runs.

The repository therefore separates:

1. **Result-reproduction utilities** – regenerate the tables/plots from the supplied result CSV files.
2. **Evaluation utilities** – calculate standard detection metrics from real prediction files.
3. **Qualitative visualization utilities** – create the severe-fog and ECAM figures when real RGB/thermal/depth/prediction/heatmap images are supplied.
4. **Dataset guidance** – explains where to obtain the public datasets referenced by the manuscript.

No public dataset is redistributed in this repository.

## Repository structure

```text
x_mftrust_reproducibility/
├── README.md
├── LICENSE
├── requirements.txt
├── .gitignore
├── CITATION.cff
├── config/
│   └── default_config.yaml
├── data/
│   ├── README_DATASETS.md
│   ├── illustrative_results.csv
│   ├── modality_contributions.csv
│   ├── hyperparameter_search.csv
│   ├── trust_scores_ci.csv
│   ├── xai_comparison.csv
│   └── uncertainty_sensitivity.csv
├── src/
│   ├── __init__.py
│   ├── metrics.py
│   ├── fog_model.py
│   ├── tables.py
│   ├── plots.py
│   └── visualization.py
├── scripts/
│   ├── reproduce_all.py
│   ├── reproduce_tables.py
│   ├── reproduce_figures.py
│   ├── evaluate_predictions.py
│   ├── generate_severe_fog_grid.py
│   └── generate_ecam_visualization.py
├── docs/
│   ├── REPRODUCTION_GUIDE.md
│   ├── DATA_PREPARATION.md
│   ├── EXPERIMENT_PROTOCOL.md
│   └── REVIEWER_REPRODUCIBILITY_NOTE.md
├── figures/
│   └── README.md
└── outputs/
    └── README.md
```

## Quick start

### 1. Create an environment

```bash
python -m venv .venv
source .venv/bin/activate
# Windows: .venv\Scripts\activate
pip install -r requirements.txt
```

### 2. Reproduce all tables and analytical figures

```bash
python scripts/reproduce_all.py
```

Generated files are written to `outputs/`.

### 3. Generate tables only

```bash
python scripts/reproduce_tables.py
```

### 4. Generate plots only

```bash
python scripts/reproduce_figures.py
```

## Dataset sources

The manuscript references VisDrone, the Teledyne FLIR Thermal Dataset, and HIT-UAV. Download them from their respective official/research distribution pages and follow their license/usage conditions. Dataset files are intentionally excluded from this repository.

See `data/README_DATASETS.md` for links and expected local directory layouts.

## Real-data evaluation

For real evaluation, prepare prediction files in CSV format with columns:

```text
image_id,class_id,confidence,x1,y1,x2,y2
```

Ground-truth CSV files use the same bounding-box representation plus a `source` or `split` field as required by your experiment. Then run:

```bash
python scripts/evaluate_predictions.py \
    --predictions path/to/predictions.csv \
    --ground-truth path/to/ground_truth.csv \
    --output outputs/evaluation.json
```

The evaluator reports precision, recall, F1 and an IoU-based AP approximation. For final journal results, use the exact detector/evaluation implementation used in the experiments and preserve the dataset's official evaluation protocol.

## Fog simulation

`src/fog_model.py` implements the atmospheric-scattering formulation used for synthetic fog augmentation:

\[
I(x)=J(x)t(x)+A(1-t(x)),\qquad t(x)=\exp(-\beta d(x)).
\]

The default beta values are:

- clear: 0.00
- light fog: 0.02
- moderate fog: 0.05
- severe fog: 0.08

These are configurable and should be calibrated to the actual visibility distribution of the experimental dataset.

## Qualitative figures

The manuscript includes two qualitative figures:

- severe-fog qualitative detection examples
- ECAM visualization and modality contribution examples

The scripts `generate_severe_fog_grid.py` and `generate_ecam_visualization.py` do not invent model predictions. They assemble supplied real images/heatmaps and supplied scores into publication-ready grids. Example/demo mode is available for layout testing only.

## Reproducibility and reporting

Before submitting the revised manuscript, replace any illustrative values with measurements from the final experiment. Record:

- dataset version and split;
- preprocessing and augmentation settings;
- random seeds;
- software versions;
- GPU/CPU configuration;
- trained checkpoint hashes;
- evaluation scripts;
- number of repeated runs;
- mean ± standard deviation and confidence intervals where applicable.

## License

The code in this repository is released under the MIT License. Dataset licenses remain with their respective dataset providers.
