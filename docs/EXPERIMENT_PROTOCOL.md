# Experimental protocol

## Illustrative configuration used in the revision draft

- Optimizer: AdamW
- Learning rate: 1e-4
- Weight decay: 1e-4
- Batch size: 16
- Epochs: 150
- Embedding dimension: 256
- Attention heads: 8
- HCMTF layers: 4
- Dropout: 0.2
- Uncertainty weight: 0.3
- Seed: 42
- Approximate inference latency: 31.6 ms/frame

Hardware/software values in the repository are also illustrative and should be replaced if the actual experimental platform differs.

## Suggested repeated-run protocol

1. Fix the dataset split.
2. Train five independent runs with controlled seeds.
3. Save checkpoints and validation curves.
4. Evaluate on the held-out test set.
5. Report mean ± standard deviation.
6. Compute confidence intervals where appropriate.
7. Preserve the exact prediction files used to compute the manuscript tables.

## Severe-fog generalization

Use a held-out severe-fog condition that is not used for model tuning. Report both aggregate metrics and representative qualitative examples. Avoid selecting qualitative examples solely because they make the model look better.
