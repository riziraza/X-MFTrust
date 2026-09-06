# Data preparation

The X-MFTrust framework is described as using RGB, thermal, LiDAR/depth and environmental information. Public datasets do not necessarily contain every modality in exactly the same synchronized form. Therefore, the actual experimental preprocessing must document how modalities were obtained, registered, synchronized, or derived.

Recommended records for every sample:

```text
sample_id
rgb_path
thermal_path
lidar_or_depth_path
environment_path
condition
split
```

For synchronized sensor pairs, use RGB as the reference stream and retain the timestamp difference. The manuscript revision used a maximum timestamp difference of 50 ms as an illustrative setting.

For LiDAR/depth projection, retain the camera intrinsics and RGB-to-LiDAR extrinsic transformation. Do not claim exact calibration parameters unless they are available from the actual experiment.

Environmental channels can include relative humidity, temperature, pressure and visibility. Store units explicitly.
