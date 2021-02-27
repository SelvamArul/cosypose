
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



2/24|23:59:13: Stats of the GT poses in dataset synpick train_pick3:
2/24|23:59:13: Number of images: 137544
2/24|23:59:13: Min dist: 868.6736945935694
2/24|23:59:13: Max dist: 16698948.167696632
2/24|23:59:14: Mean dist: 29852.629430207104
2/24|23:59:14: Min azimuth: 4.014204902193323e-06
2/24|23:59:14: Max azimuth: 359.9964916182079
2/24|23:59:14: Mean azimuth: 180.46470984288263
2/24|23:59:14: Min elev: -89.9135444119782
2/24|23:59:14: Max elev: 89.78777712170138
2/24|23:59:14: Mean elev: 5.541990926224736
2/24|23:59:14: Min visib fract: 0.0
2/24|23:59:14: Max visib fract: 1.0
2/24|23:59:15: Mean visib fract: 0.7703705662944904

2/25|00:02:16: Stats of the GT poses in dataset synpick train_move3:
2/25|00:02:16: Number of images: 99786
2/25|00:02:16: Min dist: 324.410927622508
2/25|00:02:16: Max dist: 4073655.093346596
2/25|00:02:16: Mean dist: 13735.305617782544
2/25|00:02:16: Min azimuth: 9.874140325681819e-06
2/25|00:02:16: Max azimuth: 359.9995037625184
2/25|00:02:17: Mean azimuth: 182.89217073014143
2/25|00:02:17: Min elev: -89.96415886086689
2/25|00:02:17: Max elev: 89.9556063870164
2/25|00:02:17: Mean elev: 1.6919064921861708
2/25|00:02:17: Min visib fract: 0.0
2/25|00:02:17: Max visib fract: 1.0
2/25|00:02:18: Mean visib fract: 0.6716037680618062

2/25|00:03:24: Stats of the GT poses in dataset synpick test_pick3:
2/25|00:03:24: Number of images: 31119
2/25|00:03:24: Min dist: 704.2609024895527
2/25|00:03:24: Max dist: 947621.8396044557
2/25|00:03:24: Mean dist: 2947.167611621648
2/25|00:03:24: Min azimuth: 0.026413138582290184
2/25|00:03:24: Max azimuth: 359.9983664310087
2/25|00:03:24: Mean azimuth: 176.47497654501058
2/25|00:03:24: Min elev: -89.53399399448799
2/25|00:03:24: Max elev: 89.75405912543539
2/25|00:03:24: Mean elev: 4.862434858724094
2/25|00:03:24: Min visib fract: 0.0
2/25|00:03:24: Max visib fract: 1.0
2/25|00:03:24: Mean visib fract: 0.7679706383677912

2/25|00:04:12: Stats of the GT poses in dataset synpick test_move3:
2/25|00:04:12: Number of images: 23910
2/25|00:04:12: Min dist: 1727.6299393046022
2/25|00:04:12: Max dist: 1341398.0684206423
2/25|00:04:12: Mean dist: 5064.485960255823
2/25|00:04:12: Min azimuth: 3.2679603770354496e-06
2/25|00:04:12: Max azimuth: 359.99686468974585
2/25|00:04:12: Mean azimuth: 177.93448096636342
2/25|00:04:12: Min elev: -89.9431589331172
2/25|00:04:12: Max elev: 89.92830700212497
2/25|00:04:12: Mean elev: -0.23963156633373994
2/25|00:04:12: Min visib fract: 0.0
2/25|00:04:12: Max visib fract: 1.0
2/25|00:04:12: Mean visib fract: 0.6899879899296152









cosypose training detector without pick_bad split: detector-synpick--745328
cosypose training pose without pick_bad split: synpick-refiner-finetune--666878