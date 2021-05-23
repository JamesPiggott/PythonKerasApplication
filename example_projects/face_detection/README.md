# face-recognition

### Detect on Input Image

You can detect on your image by the model. For example, detect on the image from [./data/0_Parade_marchingband_1_149.jpg](https://github.com/peteryuX/retinaface-tf2/blob/master/data/0_Parade_marchingband_1_149.jpg) as following.

```bash
python test.py --cfg_path="./configs/retinaface_res50.yaml" --img_path="./data/0_Parade_marchingband_1_149.jpg" --down_scale_factor=1.0
# or
python test.py --cfg_path="./configs/retinaface_mbv2.yaml" --img_path="./data/0_Parade_marchingband_1_149.jpg" --down_scale_factor=1.0
```

Note:
- You can down scale your input by the `--down_scale_factor`.

### Demo on Webcam

Demo face detection on your webcam.
```bash
python test.py --cfg_path="./configs/retinaface_res50.yaml" --webcam=True --down_scale_factor=1.0
# or
python test.py --cfg_path="./configs/retinaface_mbv2.yaml" --webcam=True --down_scale_factor=1.0
```


## Resources
https://www.thalesgroup.com/en/markets/digital-identity-and-security/government/biometrics/facial-recognition