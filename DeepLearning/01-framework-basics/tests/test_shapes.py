from __future__ import annotations
import unittest
try:
 import torch
except ImportError: torch=None
@unittest.skipIf(torch is None,"torch kurulu değil")
class TensorTests(unittest.TestCase):
 def test_matmul_shape(self): self.assertEqual(tuple((torch.ones(2,3)@torch.ones(3,4)).shape),(2,4))
