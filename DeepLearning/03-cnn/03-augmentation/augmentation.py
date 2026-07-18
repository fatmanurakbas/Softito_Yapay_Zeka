from __future__ import annotations
import torch
def augment(images):
 flipped=torch.flip(images,dims=[3]);noise=images+.05*torch.randn_like(images);return torch.cat([images,flipped,noise])
if __name__=="__main__":
 torch.manual_seed(1);images=torch.zeros(2,1,4,4);images[:,:,1:3,1:3]=1;out=augment(images)
 print("Önce:",tuple(images.shape),"| Sonra:",tuple(out.shape));print("Flip örneği:\n",out[2,0])
