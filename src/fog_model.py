from __future__ import annotations
import numpy as np
from PIL import Image

DEFAULT_BETA = {"clear": 0.00, "light": 0.02, "moderate": 0.05, "severe": 0.08}


def transmission(depth_m, beta):
    depth = np.maximum(np.asarray(depth_m, dtype=np.float32), 0.0)
    return np.exp(-beta * depth)


def apply_fog(rgb, depth_m, beta=0.05, airlight=1.0):
    """Apply the atmospheric-scattering fog model to an RGB image.

    rgb can be uint8 HxWx3 or float in [0,1]. depth_m must be HxW.
    """
    arr = np.asarray(rgb).astype(np.float32)
    scale = 255.0 if arr.max() > 1.5 else 1.0
    x = arr / scale
    t = transmission(depth_m, beta)[..., None]
    out = x * t + float(airlight) * (1.0 - t)
    out = np.clip(out, 0, 1) * scale
    return out.astype(np.uint8)


def load_depth(path):
    depth = np.asarray(Image.open(path)).astype(np.float32)
    return depth
