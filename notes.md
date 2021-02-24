
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
NOTE: This step is not needed.
```
python -m cosypose.scripts.run_pose_training --config synpick-refiner-syntonly
```


### pose refiner:
```
python -m cosypose.scripts.run_pose_training --config synpick-refiner-finetune
```

### eval detection:
```
CUDA_VISIBLE_DEVICES=1 python -m cosypose.scripts.run_detection_eval --config synpick
```


### /run inference (detection + pose estimation)
NOTE: This dumps the prediction. 
run eval_pose to compute evaluation metrics

```
python -m cosypose.scripts.run_synpick_inference --config synpick
```


### bob eval
```
python -m cosypose.scripts.run_bop_eval --result_id synpick--204648/dataset=synpick --method maskrcnn_detections/refiner/iteration=4
```

#### TODO:
inst_count
bop/cosypose modes: how do we define symmetry?

dict_keys(['maskrcnn_detections/coarse/iteration=1', 'maskrcnn_detections/refiner/iteration=1', 'maskrcnn_detections/refiner/iteration=2', 'maskrcnn_detections/refiner/iteration=3', 'maskrcnn_detections/refiner/iteration=4', 'maskrcnn_detections/detections'])







### FIXME:
/home/user/periyasa/workspace/cosypose/deps/bop_toolkit_cosypose/bop_toolkit_lib/dataset_params.py


export LD_LIBRARY_PATH="$LD_LIBRARY_PATH:/opt/llvm/lib"
export COSYPOSE_DIR=/home/user/periyasa/workspace/cosypose
export PYTHONPATH="/home/user/periyasa/workspace/cosypose/deps/bop_toolkit_cosypose/bop_toolkit_lib:$PYTHONPATH"

cd /home/user/periyasa/workspace/cosypose/deps/bop_toolkit_cosypose
python scripts/calc_gt_info.py