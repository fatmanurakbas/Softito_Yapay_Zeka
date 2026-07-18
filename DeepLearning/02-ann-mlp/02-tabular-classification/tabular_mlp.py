from __future__ import annotations
import torch
from torch import nn
def make_data(n=500):
    x=torch.randn(n,4); y=((x[:,0]*x[:,1]+.7*x[:,2]- .3*x[:,3])>0).float().unsqueeze(1); return x,y
if __name__ == "__main__":
    torch.manual_seed(12); x,y=make_data(); train_x,test_x=x[:400],x[400:];train_y,test_y=y[:400],y[400:]
    model=nn.Sequential(nn.Linear(4,16),nn.ReLU(),nn.Linear(16,8),nn.ReLU(),nn.Linear(8,1));opt=torch.optim.AdamW(model.parameters(),lr=.02);loss_fn=nn.BCEWithLogitsLoss()
    for _ in range(150): opt.zero_grad(); loss=loss_fn(model(train_x),train_y); loss.backward(); opt.step()
    accuracy=((torch.sigmoid(model(test_x))>=.5)==test_y).float().mean(); print(f"Test doğruluğu: {accuracy.item():.1%} | Kayıp: {loss.item():.3f}")
