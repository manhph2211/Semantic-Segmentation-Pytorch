from torch.utils.data import Dataset
import torch
import cv2
from utils import read_json

class MyDataset(Dataset) :
    def __init__(self, path, transform, size = (128,128)):
        self.data = read_json(path)
        self.size = size
        self.transform=transform

    def __getitem__(self, index):
        image = cv2.imread(list(self.data.keys())[index])
        mask = cv2.imread(list(self.data.values())[index], 0)

        image =cv2.resize(image,self.size)
        image = torch.tensor(image, dtype = torch.float32)
        image = image.permute(2,0,1)
        image = image/255
        image = self.transform(image)
        mask = cv2.resize(mask, self.size)
        mask = torch.tensor(mask, dtype= torch.int64)
        return image, mask
    def __len__(self):
        return len(self.data.keys())