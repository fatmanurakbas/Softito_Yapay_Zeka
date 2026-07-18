from __future__ import annotations
import torch
from torch import nn
if __name__=="__main__":
 image=torch.tensor([[[[0.,0.,0.,0.],[0.,1.,1.,0.],[0.,1.,1.,0.],[0.,0.,0.,0.]]]])
 conv=nn.Conv2d(1,1,kernel_size=3,bias=False);conv.weight.data=torch.tensor([[[[1.,0.,-1.],[1.,0.,-1.],[1.,0.,-1.]]]])
 print("Girdi şekli:",tuple(image.shape));print("Kernel:\n",conv.weight.detach()[0,0]);print("Çıktı:\n",conv(image).detach()[0,0])
