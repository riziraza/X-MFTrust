# Public dataset sources

The manuscript references three public datasets. Download them directly from the provider/research distribution pages and follow the applicable license and citation requirements.

## 1. VisDrone

Official dataset/download page:

https://aiskyeye.com/download/

The official VisDrone download page states that the object-detection dataset for VisDrone2024 is the same as VisDrone2019. Use the appropriate object-detection split for the manuscript experiments.

Suggested local layout:

```text
data/raw/visdrone/
├── train/images/
├── train/annotations/
├── val/images/
├── val/annotations/
├── test-dev/images/
└── test-dev/annotations/
```

## 2. Teledyne FLIR Thermal Dataset

Official dataset page:

https://oem.flir.com/solutions/automotive/adas-dataset-form/

The official page provides annotated thermal and visible-spectrum frames and indicates that the dataset includes RGB images, thermal images, and MS-COCO-formatted annotations. The download form requires information to be submitted to Teledyne FLIR.

Suggested local layout:

```text
data/raw/flir/
├── RGB/
├── thermal_8_bit/
├── thermal_16_bit/
└── annotations/
```

## 3. HIT-UAV

Research repository:

https://github.com/suojiashun/HIT-UAV-Infrared-Thermal-Dataset

The repository provides standard and oriented bounding-box annotations in XML/JSON formats and describes the high-altitude UAV infrared dataset.

Suggested local layout:

```text
data/raw/hit_uav/
├── images/
├── normal_xml/
├── normal_json/
├── rotate_xml/
└── rotate_json/
```

## Important

Do not commit downloaded datasets to the GitHub repository unless their licenses explicitly permit redistribution. This repository contains only code, metadata, and illustrative result tables.
