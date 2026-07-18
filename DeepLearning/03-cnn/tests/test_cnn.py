from __future__ import annotations
import torch,unittest
from torch import nn
class CnnTests(unittest.TestCase):
 def test_conv_shape(self):self.assertEqual(tuple(nn.Conv2d(1,4,3,padding=1)(torch.ones(2,1,8,8)).shape),(2,4,8,8))
