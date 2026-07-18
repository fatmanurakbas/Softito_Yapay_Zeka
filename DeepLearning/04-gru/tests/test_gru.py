from __future__ import annotations
import torch,unittest
from torch import nn
class GruTests(unittest.TestCase):
 def test_output_shapes(self):
  output,hidden=nn.GRU(3,5,batch_first=True)(torch.ones(2,4,3));self.assertEqual(tuple(output.shape),(2,4,5));self.assertEqual(tuple(hidden.shape),(1,2,5))
