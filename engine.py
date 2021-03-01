from utils import iou
from tqdm import tqdm


def train_fn(model, data_loader, optimizer,device,criterion):
    model.train()
    fin_loss = 0
    iou_ = 0
    for images,masks in tqdm(data_loader):
        images=images.to(device)
        masks=masks.to(device)
        optimizer.zero_grad()
        masks_hat = model(images)
        loss = criterion(masks_hat, masks)
        fin_loss += loss.item()
        iou_train = iou(masks_hat,masks)
        iou_ += iou_train
        loss.backward()
        optimizer.step()
    return fin_loss / len(data_loader), iou_/len(data_loader)


def eval_fn(model, data_loader,device,criterion):
    model.eval()
    fin_loss = 0
    iou_=0
    for images,masks in tqdm(data_loader):
        images=images.to(device)
        masks=masks.to(device)
        masks_hat=model(images)
        loss=criterion(masks_hat, masks)
        fin_loss += loss.item()
        iou_+=iou(masks_hat,masks)
    return fin_loss / len(data_loader), iou_/len(data_loader)


