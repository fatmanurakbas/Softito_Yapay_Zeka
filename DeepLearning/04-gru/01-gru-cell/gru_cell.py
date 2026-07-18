from __future__ import annotations
import torch
def sigmoid(x): return 1/(1+torch.exp(-x))
if __name__=="__main__":
 torch.manual_seed(4);x=torch.tensor([.5,-1.]);h=torch.zeros(3);wz=torch.randn(3,5)*.3;wr=torch.randn(3,5)*.3;wh=torch.randn(3,5)*.3
 combined=torch.cat([x,h]);z=sigmoid(wz@combined);r=sigmoid(wr@combined);candidate=torch.tanh(wh@torch.cat([x,r*h]));new_h=(1-z)*h+z*candidate
 print("update gate:",z.round(decimals=3).tolist());print("reset gate:",r.round(decimals=3).tolist());print("hidden:",new_h.round(decimals=3).tolist())
