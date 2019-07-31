#!/usr/bin/env python

__author__ = "marked@gmail.com (Mark Rosetta)"
__version__ = "1.0"

"""Unit test for primes.py"""

import prime_bits
import unittest

class PrimeBitsTestCase(unittest.TestCase):
  def testDistCache(self):
    pb = prime_bits.PrimeBits()
    self.assertEqual(pb.dist_get_cache(0), [ 1 ])
    self.assertEqual(pb.dist_get_cache(1), [ 1, 1 ])
    self.assertEqual(pb.dist_get_cache(2), [ 1, 2, 1 ])
    self.assertEqual(pb.dist_get_cache(3), [ 1, 3, 3, 1 ])

    
  def testUnfilteredDist(self):
    pb = prime_bits.PrimeBits( prefilter=False )
    self.assertEqual(pb.dist(0), [ 1 ])
    self.assertEqual(pb.dist(1), [ 1, 1 ])
    self.assertEqual(pb.dist(2), [ 1, 2 ])
    self.assertEqual(pb.dist(3), [ 1, 2, 1 ] )
    self.assertEqual(pb.dist(7), [ 1, 3, 3, 1 ] )
    self.assertEqual(pb.dist(8), [ 1, 4, 3, 1 ] )
    self.assertEqual(pb.dist(9), [ 1, 4, 4, 1 ] )
    self.assertEqual(pb.dist(10), [ 1, 4, 5, 1 ] )
    self.assertEqual(pb.dist(7, 7),   [ 0, 0, 0, 1 ] )
    self.assertEqual(pb.dist(8, 8),   [ 0, 1, 0, 0 ] )
    self.assertEqual(pb.dist(9, 9),   [ 0, 0, 1, 0 ] )
    self.assertEqual(pb.dist(127, 1), [0, 7, 21, 35, 35, 21, 7, 1] )
    self.assertEqual(pb.dist(127, 0), [1, 7, 21, 35, 35, 21, 7, 1] )
    self.assertEqual(pb.dist(2**8-1, 2**8-1), [0, 0, 0, 0, 0, 0, 0, 0, 1] )
    self.assertEqual(pb.dist(2**7-1, 2**7-1), [0, 0, 0, 0, 0, 0, 0, 1] )
    
  def testPrefilteredDist(self):
    pb = prime_bits.PrimeBits( prefilter=True )
    self.assertEqual(pb.dist(0), [ ])
    self.assertEqual(pb.dist(1), [ ])
    self.assertEqual(pb.dist(2), [ ])
    self.assertEqual(pb.dist(3), [ 1 ] )
    self.assertEqual(pb.dist(7), [ 3, 1 ] )
    self.assertEqual(pb.dist(8), [ 3, 1 ] )
    self.assertEqual(pb.dist(9), [ 4, 1 ] )
    self.assertEqual(pb.dist(10), [ 5, 1 ] )
    self.assertEqual(pb.dist(7, 7),   [ 0, 1 ] )
    self.assertEqual(pb.dist(8, 8),   [ 0, 0 ] )
    self.assertEqual(pb.dist(9, 9),   [ 1, 0 ] )
    self.assertEqual(pb.dist(127, 1), [ 21, 35, 21, 1 ] )
    self.assertEqual(pb.dist(2**8-1, 2**8-1), [ 0, 0, 0, 0 ] )
    self.assertEqual(pb.dist(2**7-1, 2**7-1), [ 0, 0, 0, 1 ] )
    
  def testFilterSame(self):
    uf = prime_bits.PrimeBits( prefilter=False )
    pf = prime_bits.PrimeBits( prefilter=True )
    for i in range(0, 1000):
      self.assertEqual(uf.primes.prime_mask(uf.dist(i+10, i)), pf.dist(i+10, i))

  def testCacheSame(self):
    pb = prime_bits.PrimeBits()
    for i in range(0, 100):
      self.assertEqual(pb.dist_get_cache(i), pb.dist(2**i-1))
    
  def testPrimeBits(self):
    pb = prime_bits.PrimeBits()
    self.assertEqual(pb.prime_bits(4, 10), 5)
    self.assertEqual(pb.prime_bits(0, 0), 0)
    self.assertEqual(pb.prime_bits(1, 1), 0)
    self.assertEqual(pb.prime_bits(2, 2), 0)
    self.assertEqual(pb.prime_bits(3, 3), 1)
    self.assertEqual(pb.prime_bits(4, 4), 0)
    self.assertEqual(pb.prime_bits(1, 10), 6)
    self.assertEqual(pb.prime_bits(0, 10), 6)
    self.assertEqual(pb.prime_bits(0, 1), 0)
    self.assertEqual(pb.prime_bits(2**1024-1, 2**1024-1), 0)
  
  def testInput(self):
    pb = prime_bits.PrimeBits()
    self.assertRaises(Exception, pb.dist, 1, 10)
    self.assertRaises(Exception, pb.dist, 10, -1)
    self.assertRaises(Exception, pb.dist, -10, 1)

if __name__ == "__main__":
  unittest.main()
