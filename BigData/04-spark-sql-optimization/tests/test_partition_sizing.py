from __future__ import annotations
import math,unittest
class SizingTests(unittest.TestCase):
 def test_500gb_at_256mb(self):self.assertEqual(math.ceil(500*1024/256),2000)
