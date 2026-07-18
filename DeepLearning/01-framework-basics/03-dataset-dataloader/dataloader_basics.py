from __future__ import annotations
import torch
from torch.utils.data import DataLoader,TensorDataset
if __name__ == "__main__":
    features=torch.arange(12,dtype=torch.float32).reshape(6,2); labels=torch.tensor([0,1,0,1,0,1])
    loader=DataLoader(TensorDataset(features,labels),batch_size=2,shuffle=False)
    for index,(x,y) in enumerate(loader,1): print(f"batch {index}: x={x.tolist()} y={y.tolist()}")
