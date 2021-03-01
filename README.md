# An implementation of UNet - Pytorch

## 0. Introduction :smiley:

- This repo is about implementing normal UNet in the task of **semantic segmentation** from scratch!

![alt text](https://github.com/manhph2211/Semantic-Segmentation-Pytorch/blob/main/UNet.png)


- Okey, let's start with:

  - `git clone https://github.com/manhph2211/Semantic-Segmentation-Pytorch.git` 
  - `cd Semantic-Segmentation-Pytorch`


## 1. Data :smiley:

You'll make your own dataset in this task. But first, `cd data`

### 1.1 Images 

- First of all, I used `google_images_download` which is a tool for downloading images from google-image. One way to to this is copying folder `./google_images_download` in [this amazing repo](https://github.com/hardikvasa/google-images-download) to your folder `./data` . 

- Then open `create_data.py` , `keywords` and `limit` is up to you!. Save and Run it to get images in `./download/keywords` . Oh note that if you want to get more than 100 images, you might need to refer [this](https://github.com/hardikvasa/google-images-download/issues/53)

### 1.2 Annotations 

- In this task, I used [this website](https://cvat.org/) to label the downloaded images above and then dump them as annotations, note that annotations should be saved in `./data`. Then just following:
```
mkdir mask && cd mask
cd ../..
python3 utils.py
```

- One other way to get annotations of our images that I find quite interesting, refer to [this](https://github.com/abreheret/PixelAnnotationTool?fbclid=IwAR1va_pH7DMsCWKkftSeGP7SGkGPS4TB_0ZPKHHHXqe8Ute-ovLdqe1q0O0)

## 2. Dependencies :smile:

- torch
- torchvision
- Python-opencv
- sklearn
- pycocotools
- matplotlib
- numpy
- pandas
- tqdm

## 3. Train & Prediction  :smiley:

- Just run `python3 train.py`
- `python3 test.py`
