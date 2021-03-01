import cv2
import matplotlib.pyplot as plt
from utils import read_json
import torch
from model import UNET
from train import test_data


def test(model,test_data):
    imgs,masks=next(iter(test_data))
    mask=model(imgs[0])
    f, axarr = plt.subplots(2, 2)
    axarr[0, 0].imshow(imgs[0])
    axarr[0, 1].imshow(mask)
    plt.show()


if __name__=="__main__":

    model=UNET()
    PATH='./weights/unet_best_val.pth'
    model.load_state_dict(torch.load(PATH))
    test(model,test_data)