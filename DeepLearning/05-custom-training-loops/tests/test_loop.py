from __future__ import annotations
import torch,unittest
from torch import nn
class LoopTests(unittest.TestCase):
 def test_optimizer_changes_weight(self):
  model=nn.Linear(1,1);before=model.weight.detach().clone();opt=torch.optim.SGD(model.parameters(),lr=.1);loss=(model(torch.ones(2,1))-torch.zeros(2,1)).pow(2).mean();opt.zero_grad();loss.backward();opt.step();self.assertFalse(torch.equal(before,model.weight))
