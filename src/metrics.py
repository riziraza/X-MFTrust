from __future__ import annotations
import numpy as np
from sklearn.metrics import precision_score, recall_score, f1_score


def classification_metrics(y_true, y_pred):
    return {
        "precision": precision_score(y_true, y_pred, zero_division=0),
        "recall": recall_score(y_true, y_pred, zero_division=0),
        "f1": f1_score(y_true, y_pred, zero_division=0),
    }


def box_iou(box_a, box_b):
    ax1, ay1, ax2, ay2 = box_a
    bx1, by1, bx2, by2 = box_b
    ix1, iy1 = max(ax1, bx1), max(ay1, by1)
    ix2, iy2 = min(ax2, bx2), min(ay2, by2)
    iw, ih = max(0.0, ix2 - ix1), max(0.0, iy2 - iy1)
    inter = iw * ih
    area_a = max(0.0, ax2-ax1) * max(0.0, ay2-ay1)
    area_b = max(0.0, bx2-bx1) * max(0.0, by2-by1)
    union = area_a + area_b - inter
    return inter / union if union else 0.0


def detection_prf(predictions, ground_truths, iou_threshold=0.5):
    """Greedy IoU matching for a transparent baseline evaluation.

    Each item must be a dict with image_id, class_id and bbox=[x1,y1,x2,y2].
    Predictions may additionally contain confidence.
    """
    gt_used = set()
    tp = fp = 0
    for p in sorted(predictions, key=lambda x: x.get("confidence", 1.0), reverse=True):
        best = (-1.0, None)
        for i, g in enumerate(ground_truths):
            if i in gt_used or g["image_id"] != p["image_id"] or g["class_id"] != p["class_id"]:
                continue
            iou = box_iou(p["bbox"], g["bbox"])
            if iou > best[0]:
                best = (iou, i)
        if best[0] >= iou_threshold:
            tp += 1
            gt_used.add(best[1])
        else:
            fp += 1
    fn = len(ground_truths) - tp
    precision = tp/(tp+fp) if tp+fp else 0.0
    recall = tp/(tp+fn) if tp+fn else 0.0
    f1 = 2*precision*recall/(precision+recall) if precision+recall else 0.0
    return {"precision": precision, "recall": recall, "f1": f1, "tp": tp, "fp": fp, "fn": fn}
