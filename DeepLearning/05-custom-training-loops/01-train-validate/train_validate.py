from __future__ import annotations
import torch
from torch import nn
from torch.utils.data import DataLoader,TensorDataset
def make_loader(n):
 x=torch.randn(n,3);y=(x.sum(1)>0).long();return DataLoader(TensorDataset(x,y),batch_size=16,shuffle=True)
def evaluate(model,loader,loss_fn):
 model.eval();losses=[];correct=total=0
 with torch.no_grad():
  for x,y in loader:
   logits=model(x);losses.append(loss_fn(logits,y).item());correct+=(logits.argmax(1)==y).sum().item();total+=len(y)
 return sum(losses)/len(losses),correct/total
if __name__=="__main__":
 torch.manual_seed(21);train,val=make_loader(160),make_loader(60);model=nn.Sequential(nn.Linear(3,12),nn.ReLU(),nn.Linear(12,2));opt=torch.optim.Adam(model.parameters(),lr=.03);loss_fn=nn.CrossEntropyLoss()
 for epoch in range(1,16):
  model.train();losses=[]
  for x,y in train:opt.zero_grad();loss=loss_fn(model(x),y);loss.backward();opt.step();losses.append(loss.item())
  if epoch in (1,5,10,15):v_loss,v_acc=evaluate(model,val,loss_fn);print(f"epoch={epoch:2} train_loss={sum(losses)/len(losses):.3f} val_loss={v_loss:.3f} val_acc={v_acc:.1%}")
