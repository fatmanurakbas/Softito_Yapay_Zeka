from __future__ import annotations
import torch
from torch import nn
def data(n=300):
 x=torch.randn(n,6);return x,((x[:,:3].sum(1)+.4*torch.randn(n))>0).float().unsqueeze(1)
def train(model,x,y):
 opt=torch.optim.Adam(model.parameters(),lr=.02);loss_fn=nn.BCEWithLogitsLoss()
 for _ in range(100): opt.zero_grad();loss=loss_fn(model(x),y);loss.backward();opt.step()
 return model
if __name__=="__main__":
 torch.manual_seed(3);x,y=data();tx,vx=x[:220],x[220:];ty,vy=y[:220],y[220:]
 models={"temel":nn.Sequential(nn.Linear(6,32),nn.ReLU(),nn.Linear(32,1)),"dropout+batchnorm":nn.Sequential(nn.Linear(6,32),nn.BatchNorm1d(32),nn.ReLU(),nn.Dropout(.25),nn.Linear(32,1))}
 for name,model in models.items():
  train(model,tx,ty);model.eval();acc=((torch.sigmoid(model(vx))>=.5)==vy).float().mean();print(f"{name}: doğrulama doğruluğu={acc.item():.1%}")
