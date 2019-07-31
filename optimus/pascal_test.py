#!/usr/bin/env python2

__author__ = "marked@gmail.com (Mark Rosetta)"
__version__ = "1.0"

"""Unit test for pascal.py"""

import pascal
import unittest

class PascalTestCase(unittest.TestCase):
  def testGetRow(self):
    p = pascal.Pascal()
    self.assertEqual(p.get_row(0), [ 1 ])
    self.assertEqual(p.get_row(1), [ 1, 1 ])
    self.assertEqual(p.get_row(2), [ 1, 2, 1 ])
    self.assertEqual(p.get_row(3), [ 1, 3, 3, 1 ])
    
  def testMax(self):
    p = pascal.Pascal(64)
    self.assertEqual(p.get_max(), 64)

if __name__ == "__main__":
  unittest.main()
