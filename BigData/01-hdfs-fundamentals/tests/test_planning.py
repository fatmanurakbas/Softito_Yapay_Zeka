from __future__ import annotations
import math,unittest
class HdfsPlanningTests(unittest.TestCase):
 def test_block_count(self):self.assertEqual(math.ceil(1024/128),8)
 def test_partial_block(self):self.assertEqual(math.ceil(129/128),2)
