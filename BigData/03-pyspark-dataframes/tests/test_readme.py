from __future__ import annotations
from pathlib import Path
import unittest
ROOT=Path(__file__).resolve().parents[1]
class StructureTests(unittest.TestCase):
 def test_exercise_files(self):
  self.assertTrue(all((ROOT/path).is_file() for path in ["01-transformations/dataframe_transformations.py","02-spark-sql/spark_sql.py","03-joins/joins.py","04-window-functions/window_functions.py"]))
