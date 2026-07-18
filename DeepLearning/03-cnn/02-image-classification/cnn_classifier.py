from __future__ import annotations
import torch
from torch import nn
def make_images(n=160):
 x=.08*torch.randn(n,1,8,8);y=torch.arange(n)%2
 for i,label in enumerate(y):
  if label==0:x[i,0,:,3:5]+=1
  else:x[i,0,3:5,:]+=1
 return x,y
if __name__=="__main__":
 torch.manual_seed(9);x,y=make_images();tx,vx=x[:120],x[120:];ty,vy=y[:120],y[120:]
 model=nn.Sequential(nn.Conv2d(1,4,3,padding=1),nn.ReLU(),nn.MaxPool2d(2),nn.Conv2d(4,8,3,padding=1),nn.ReLU(),nn.AdaptiveAvgPool2d(1),nn.Flatten(),nn.Linear(8,2));opt=torch.optim.Adam(model.parameters(),lr=.02);loss_fn=nn.CrossEntropyLoss()
 for _ in range(35):opt.zero_grad();loss=loss_fn(model(tx),ty);loss.backward();opt.step()
 acc=(model(vx).argmax(1)==vy).float().mean();print(f"Validation doğruluğu: {acc.item():.1%} | Kayıp: {loss.item():.4f}")
