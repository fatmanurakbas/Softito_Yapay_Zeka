from __future__ import annotations
import torch
from torch import nn
def data(n=160):
 x=torch.randn(n,6,3);y=(x[:,-2:,0].sum(1)>0).long();return x,y
if __name__=="__main__":
 torch.manual_seed(17);x,y=data();tx,vx=x[:120],x[120:];ty,vy=y[:120],y[120:]
 class Classifier(nn.Module):
  def __init__(self):super().__init__();self.gru=nn.GRU(3,12,batch_first=True);self.head=nn.Linear(12,2)
  def forward(self,x):_,hidden=self.gru(x);return self.head(hidden[-1])
 model=Classifier();opt=torch.optim.Adam(model.parameters(),lr=.02);loss_fn=nn.CrossEntropyLoss()
 for _ in range(50):opt.zero_grad();loss=loss_fn(model(tx),ty);loss.backward();opt.step()
 print(f"Validation doğruluğu: {(model(vx).argmax(1)==vy).float().mean().item():.1%} | Kayıp: {loss.item():.3f}")
