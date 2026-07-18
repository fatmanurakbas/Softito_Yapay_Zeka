from __future__ import annotations
import unittest,torch
from torch import nn
class MlpTests(unittest.TestCase):
 def test_output_shape(self): self.assertEqual(tuple(nn.Linear(3,1)(torch.ones(2,3)).shape),(2,1))
