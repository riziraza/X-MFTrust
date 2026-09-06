from __future__ import annotations
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont
import pandas as pd


def _load(path, size):
    img = Image.open(path).convert("RGB")
    return img.resize(size)


def make_severe_fog_grid(rows, output, cell=(320,180)):
    """Create the manuscript-style severe-fog qualitative grid.

    rows: list of dictionaries with keys rgb, thermal, depth, prediction,
    heatmap, trust, and optional label.
    """
    labels = ["RGB Input", "Thermal Observation", "Depth Representation", "Predicted Detection", "Explanation Heatmap", "Trust Score"]
    margin, header, gap = 20, 45, 8
    width = margin*2 + 6*cell[0] + 5*gap
    height = margin*2 + header + len(rows)*cell[1] + (len(rows)-1)*gap
    canvas = Image.new("RGB", (width,height), "white")
    d = ImageDraw.Draw(canvas)
    font = ImageFont.load_default()
    for j, lab in enumerate(labels):
        x = margin + j*(cell[0]+gap)
        d.text((x+8, 15), lab, fill="black", font=font)
    for i, row in enumerate(rows):
        y = margin + header + i*(cell[1]+gap)
        for j, key in enumerate(["rgb","thermal","depth","prediction","heatmap"]):
            x = margin + j*(cell[0]+gap)
            canvas.paste(_load(row[key], cell), (x,y))
        x = margin + 5*(cell[0]+gap)
        d.rounded_rectangle((x,y,x+cell[0],y+cell[1]), radius=12, outline="gray", width=2)
        trust = row.get("trust", "")
        d.text((x+cell[0]//3,y+cell[1]//2), str(trust), fill="black", font=font)
    canvas.save(output, quality=95)


def make_ecam_grid(rows, output, cell=(210,150)):
    labels = ["Condition", "RGB", "Thermal", "LiDAR", "Environmental", "ECAM-RGB", "ECAM-Thermal", "ECAM-LiDAR", "ECAM-Env.", "Contributions"]
    margin, header, gap = 12, 35, 5
    width = margin*2 + 10*cell[0] + 9*gap
    height = margin*2 + header + len(rows)*cell[1] + (len(rows)-1)*gap
    canvas = Image.new("RGB", (width,height), "white")
    d = ImageDraw.Draw(canvas); font = ImageFont.load_default()
    for j, lab in enumerate(labels):
        x = margin + j*(cell[0]+gap); d.text((x+4,10),lab,fill="black",font=font)
    for i,row in enumerate(rows):
        y = margin + header + i*(cell[1]+gap)
        d.text((margin+5,y+cell[1]//2),row.get("condition",""),fill="black",font=font)
        keys=["rgb","thermal","lidar","environment","ecam_rgb","ecam_thermal","ecam_lidar","ecam_environment"]
        for j,key in enumerate(keys, start=1):
            x=margin+j*(cell[0]+gap); canvas.paste(_load(row[key],cell),(x,y))
        x=margin+9*(cell[0]+gap)
        d.rounded_rectangle((x,y,x+cell[0],y+cell[1]),radius=8,outline="gray",width=2)
        scores=row.get("contributions",{})
        d.text((x+8,y+10),str(scores),fill="black",font=font)
    canvas.save(output,quality=95)
