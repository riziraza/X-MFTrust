from pathlib import Path
import argparse, json, pandas as pd, sys
ROOT=Path(__file__).resolve().parents[1]; sys.path.insert(0,str(ROOT))
from src.metrics import detection_prf


def load_pred(path):
    df=pd.read_csv(path); out=[]
    for _,r in df.iterrows():
        out.append({"image_id":str(r.image_id),"class_id":int(r.class_id),"confidence":float(r.confidence),"bbox":[float(r.x1),float(r.y1),float(r.x2),float(r.y2)]})
    return out


def load_gt(path):
    df=pd.read_csv(path); out=[]
    for _,r in df.iterrows():
        out.append({"image_id":str(r.image_id),"class_id":int(r.class_id),"bbox":[float(r.x1),float(r.y1),float(r.x2),float(r.y2)]})
    return out

if __name__ == "__main__":
    ap=argparse.ArgumentParser()
    ap.add_argument("--predictions",required=True)
    ap.add_argument("--ground-truth",required=True)
    ap.add_argument("--iou",type=float,default=0.5)
    ap.add_argument("--output",default="outputs/evaluation.json")
    a=ap.parse_args()
    result=detection_prf(load_pred(a.predictions),load_gt(a.ground_truth),a.iou)
    Path(a.output).parent.mkdir(parents=True,exist_ok=True)
    Path(a.output).write_text(json.dumps(result,indent=2))
    print(json.dumps(result,indent=2))
