
## General notes

### BOP introduced these changes to the models:

The 3D models were converted from meters to millimeters and the centers of their 3D bounding boxes were aligned with the origin of the model coordinate system. This transformation was reflected also in the ground-truth poses. The models were transformed so they follow the same conventions as models from other datasets included in BOP and are thus compatible with the BOP toolkit.
We additionally provide 50K PBR training images that were generated for the BOP Challenge 2020. 
And also considered 002_master_chef_can and 040_large_marker as symmetric.

### models_bop-compat: (introduced by cosypose)
In the BOP format, the YCB objects 002_master_chef_can and 040_large_marker are considered symmetric, but not by previous works such as PoseCNN, PVNet and DeepIM. To ensure a fair comparison (using ADD instead of ADD-S for ADD-(S) for these objects), these objects must not be considered symmetric in the evaluation. To keep the uniformity of the models format, we generate a set of YCB objects models_bop-compat_eval that can be used to fairly compare our approach against previous works. You can download them directly:





## Training details
```
runjob --ngpus=32 python -m cosypose.scripts.run_detector_training --config bop-DATASET-TRAINING_IMAGES
where DATASET={lmo,tless,tudl,icbin,itodd,hb,ycbv} and TRAINING_IMAGES={pbr,synt+real} (synt+real only for datasets where real images are available: tless, tudl and ycbv).
```

### detector:
```
CUDA_VISIBLE_DEVICES=2,3 python -m cosypose.scripts.run_detector_training --config bop-ycbv-synt+real
```


## Synpick specific:
 
```
DATASET= synpick
TRAINING_IMAGES= synt (only synt exists)
```

### Train detector:
```
CUDA_VISIBLE_DEVICES=2 python -m cosypose.scripts.run_detector_training --config synpick-synt
```

### pose coarse:
```
python -m cosypose.scripts.run_pose_training --config ycbv-refiner-syntonly
```


### pose refiner:
```
python -m cosypose.scripts.run_pose_training --config ycbv-refiner-finetune
```