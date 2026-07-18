from __future__ import annotations
import torch
if __name__ == "__main__":
    device=torch.device("cuda" if torch.cuda.is_available() else "cpu")
    x=torch.tensor([[1.,2.],[3.,4.]],device=device); y=torch.ones_like(x)
    print("Cihaz:",device,"| şekil:",x.shape,"| dtype:",x.dtype); print("x + y =\n",x+y); print("matris çarpımı=\n",x@x)
