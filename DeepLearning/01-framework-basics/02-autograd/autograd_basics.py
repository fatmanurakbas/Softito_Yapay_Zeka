from __future__ import annotations
import torch
if __name__ == "__main__":
    x=torch.tensor([2.0,-3.0],requires_grad=True); loss=(x**2).sum(); loss.backward()
    print("loss:",loss.item(),"| gradient:",x.grad.tolist(),"| beklenen:",[4.0,-6.0])
