from __future__ import annotations
import torch
from torch import nn
if __name__ == "__main__":
    torch.manual_seed(7); x=torch.tensor([[0.,0.],[0.,1.],[1.,0.],[1.,1.]]); y=torch.tensor([[0.],[1.],[1.],[0.]])
    model=nn.Sequential(nn.Linear(2,8),nn.Tanh(),nn.Linear(8,1)); opt=torch.optim.Adam(model.parameters(),lr=.08); loss_fn=nn.BCEWithLogitsLoss()
    for _ in range(500): opt.zero_grad(); loss=loss_fn(model(x),y); loss.backward(); opt.step()
    print("Kayıp:",round(loss.item(),4)); print("Tahmin:",torch.sigmoid(model(x)).detach().round(decimals=3).flatten().tolist())
