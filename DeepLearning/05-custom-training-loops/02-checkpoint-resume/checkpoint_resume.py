from __future__ import annotations
import torch
from torch import nn
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
if __name__=="__main__":
 torch.manual_seed(2);model=nn.Linear(2,1);optimizer=torch.optim.SGD(model.parameters(),lr=.1);x=torch.randn(20,2);y=x.sum(1,keepdim=True)
 for _ in range(10):optimizer.zero_grad();loss=((model(x)-y)**2).mean();loss.backward();optimizer.step()
 path=ROOT/"checkpoints"/"latest.pt";torch.save({"epoch":10,"model_state":model.state_dict(),"optimizer_state":optimizer.state_dict(),"loss":loss.item()},path)
 restored=nn.Linear(2,1);state=torch.load(path,weights_only=True);restored.load_state_dict(state["model_state"]);print(f"Checkpoint: epoch={state['epoch']} loss={state['loss']:.4f} | {path.name}")
