import torch
from torch.utils.data import DataLoader
from dataset import MyDataset
from model import UNET
from torch.optim import Adam
from torch.nn import CrossEntropyLoss
from torchvision import transforms
from engine import train_fn,eval_fn
from tqdm import tqdm
import pandas as pd


device = torch.device("cuda:0" if torch.cuda.is_available() else "cpu")
print("device:", device)

TRAIN_JSON_DATA_PATH = './data/train_data.json'
VAL_JSON_DATA_PATH = './data/val_data.json'
TEST_JSON_DATA_PATH = './data/test_data.json'

BATCH_SIZE = 4
transform=transforms.Compose([transforms.Normalize((0.5, 0.5, 0.5), (0.5, 0.5, 0.5))])

train_data_dataset = MyDataset(TRAIN_JSON_DATA_PATH,transform)
train_data = DataLoader(train_data_dataset, batch_size=BATCH_SIZE,shuffle=True)

val_data_dataset = MyDataset(VAL_JSON_DATA_PATH,transform)
val_data = DataLoader(val_data_dataset, batch_size=BATCH_SIZE,shuffle=False)

test_data_dataset = MyDataset(TEST_JSON_DATA_PATH,transform)
test_data = DataLoader(test_data_dataset, batch_size=BATCH_SIZE,shuffle=False)

# Model
model = UNET()
MODEL_SAVE_PATH = './weights/weights.pt'
model.to(device)
N_EPOCHS = 20
optimizer = Adam(model.parameters())
criterion = CrossEntropyLoss()
best_val_loss=999
print("Training...")
for epoch in range(N_EPOCHS):
    log=[]
    loss_train_epoch,iou_train_epoch= train_fn(model,train_data,optimizer,device,criterion)
    loss_val_epoch,iou_val_epoch=eval_fn(model,val_data,device,criterion)
    log_epoch = {"epoch": epoch + 1, "train_loss": loss_train_epoch,"train_iou":iou_train_epoch, "val_loss": loss_val_epoch,"val_iou":iou_val_epoch}
    log.append(log_epoch)
    df = pd.DataFrame(log)
    df.to_csv("./logs.csv")
    #torch.save(model.state_dict(), "./weights/unet" + ".pth")
    if loss_val_epoch < best_val_loss:
        best_val_loss = loss_val_epoch
        torch.save(model.state_dict(), "./weights/unet_best_val" + ".pth")
    print("Epoch {} || epoch_train_loss: {:.4f} || Epoch_train_iou: {:.4f} || Epoch_val_loss: {:.4f} || Epoch_val_iou; {:.4f} ".format(epoch + 1,loss_train_epoch,iou_train_epoch,loss_val_epoch,iou_val_epoch))
