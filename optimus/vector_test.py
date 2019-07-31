#!/usr/bin/env python2

__author__ = "marked@gmail.com (Mark Rosetta)"
__version__ = "1.0"

"""Unit test for vector.py"""

import vector
import unittest

class VectorTestCase(unittest.TestCase):
  def testAdd(self):
    self.assertEqual(vector.add( [ 0, 0, 0 ], [ 1, 1, 1 ] ), [ 1, 1, 1 ] )
    self.assertEqual(vector.add( [ 1, 2, 3 ], [ 4, 5, 6 ] ), [ 5, 7, 9 ] ) 
    self.assertEqual(vector.add( [ 10, 20, 30 ], [ 1, 2 ] ), [ 11, 22, 30 ] )
    self.assertEqual(vector.add( [ 1, 2 ], [ 10, 20, 30 ] ), [ 11, 22, 30 ] )

  def testMinus(self):
    self.assertEqual(vector.minus( [5, 7, 9], [4, 5, 6] ), [1, 2, 3] )
    self.assertEqual(vector.minus( [5, 7, 9], [1, 2] ), [4, 5, 9] )
    self.assertEqual(vector.minus( [1, 2], [5, 7, 9] ), [-4, -5, -9] )
    
  def testShift(self):
    self.assertEqual(vector.shift( [1, 2, 3 ], 0), [1, 2, 3])
    self.assertEqual(vector.shift( [1, 2, 3 ], 1), [0, 1, 2, 3])
    
if __name__ == "__main__":
  unittest.main()
