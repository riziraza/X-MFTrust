# Reproduction guide

## A. Regenerate the manuscript result tables

Run:

```bash
python scripts/reproduce_tables.py
```

This creates Markdown and LaTeX versions under `outputs/tables/`.

## B. Regenerate analytical plots

Run:

```bash
python scripts/reproduce_figures.py
```

The scripts read the CSV files in `data/` and generate 300-dpi PNG figures.

## C. Reproduce qualitative severe-fog figure

Create a JSON manifest such as:

```json
[
  {
    "rgb": "data/qualitative/row1_rgb.png",
    "thermal": "data/qualitative/row1_thermal.png",
    "depth": "data/qualitative/row1_depth.png",
    "prediction": "data/qualitative/row1_prediction.png",
    "heatmap": "data/qualitative/row1_heatmap.png",
    "trust": "0.87 (High)"
  }
]
```

Then:

```bash
python scripts/generate_severe_fog_grid.py --manifest severe_fog_manifest.json
```

The script assembles the supplied real outputs; it does not generate detections itself.

## D. Reproduce ECAM visualization

Prepare a manifest containing RGB, thermal, LiDAR, environmental and four ECAM heatmap images plus contribution scores. Then run:

```bash
python scripts/generate_ecam_visualization.py --manifest ecam_manifest.json
```

## E. Replace illustrative results

The files under `data/` contain the values used in the revision draft. Replace them with actual measurements after running the final experiments. Keep the column names unchanged so the scripts remain compatible.
