#!/usr/bin/env python2

__author__ = "marked@gmail.com (Mark Rosetta)"
__version__ = "1.0"

""" Unit test for bit.py """

import bit
import unittest

class BitTestCase(unittest.TestCase):
  
  def testList(self):
    """list() should give bit represention of input in a list"""
    self.assertEqual(bit.list(0), [ 0 ])
    self.assertEqual(bit.list(1), [ 1 ])
    self.assertEqual(bit.list(2), [ 1, 0 ])
    self.assertEqual(bit.list(3), [ 1, 1 ])
    self.assertEqual(bit.list(4), [ 1, 0, 0 ])
    self.assertEqual(bit.list(10), [ 1, 0, 1, 0 ])

  def testWidth(self):
    """width() should give # of bits needed to represent input"""
    self.assertEqual(bit.width(0), 1)
    self.assertEqual(bit.width(1), 1)
    self.assertEqual(bit.width(2), 2)
    self.assertEqual(bit.width(3), 2)
    self.assertEqual(bit.width(4), 3)
    self.assertEqual(bit.width(100), 7)
    self.assertEqual(bit.width(127), 7)
    self.assertEqual(bit.width(128), 8)
    self.assertEqual(bit.width(129), 8)

if __name__ == "__main__":
  unittest.main()