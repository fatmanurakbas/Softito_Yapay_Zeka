from __future__ import annotations
import torch
from torch import nn
def gradient_norm(model):return torch.sqrt(sum((p.grad**2).sum() for p in model.parameters() if p.grad is not None))
if __name__=="__main__":
 torch.manual_seed(5);model=nn.Sequential(nn.Linear(4,32),nn.ReLU(),nn.Linear(32,1));opt=torch.optim.Adam(model.parameters(),lr=.02);x=torch.randn(32,4);y=torch.randn(32,1);accumulation_steps=4
 opt.zero_grad()
 for index in range(accumulation_steps):
  loss=((model(x[index*8:(index+1)*8])-y[index*8:(index+1)*8])**2).mean()/accumulation_steps;loss.backward()
 before=gradient_norm(model).item();torch.nn.utils.clip_grad_norm_(model.parameters(),max_norm=.5);after=gradient_norm(model).item();opt.step();print(f"Gradient norm: {before:.3f} -> {after:.3f} | accumulation={accumulation_steps}")
