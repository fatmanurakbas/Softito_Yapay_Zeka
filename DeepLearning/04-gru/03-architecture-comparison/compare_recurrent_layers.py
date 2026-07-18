from __future__ import annotations
from torch import nn
def count(module):return sum(p.numel() for p in module.parameters())
if __name__=="__main__":
 input_size,hidden=8,16
 for name,layer in (("RNN",nn.RNN(input_size,hidden,batch_first=True)),("GRU",nn.GRU(input_size,hidden,batch_first=True)),("LSTM",nn.LSTM(input_size,hidden,batch_first=True))):print(f"{name}: {count(layer)} parametre")
