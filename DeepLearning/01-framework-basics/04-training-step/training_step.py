from __future__ import annotations
import torch
from torch import nn
if __name__ == "__main__":
    torch.manual_seed(42); x=torch.tensor([[0.,0.],[0.,1.],[1.,0.],[1.,1.]]); y=torch.tensor([[0.],[1.],[1.],[1.]])
    model=nn.Sequential(nn.Linear(2,4),nn.ReLU(),nn.Linear(4,1)); optimizer=torch.optim.SGD(model.parameters(),lr=0.2); loss_fn=nn.BCEWithLogitsLoss()
    for epoch in range(100):
        optimizer.zero_grad(); loss=loss_fn(model(x),y); loss.backward(); optimizer.step()
    print("Son kayıp:",round(loss.item(),4)); print("Olasılıklar:",torch.sigmoid(model(x)).detach().flatten().round(decimals=3).tolist())
