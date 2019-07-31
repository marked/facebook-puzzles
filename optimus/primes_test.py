#!/usr/bin/env python2

__author__ = "marked@gmail.com (Mark Rosetta)"
__version__ = "1.0"

""" Unit test for primes.py """

import primes
import unittest

class PrimesTestCase(unittest.TestCase):
  def testSieve(self):
    p = primes.Primes()

    self.assertEqual(p.sieve(0), [ 0 ])
    self.assertEqual(p.sieve(1), [ 0, 0 ])
    self.assertEqual(p.sieve(2), [ 0, 0, 2 ])
    self.assertEqual(p.sieve(3), [ 0, 0, 2, 3 ])
    self.assertEqual(p.sieve(4), [ 0, 0, 2, 3, 0 ])
    self.assertEqual(p.sieve(5), [ 0, 0, 2, 3, 0, 5 ])
    self.assertEqual(p.sieve(6), [ 0, 0, 2, 3, 0, 5, 0 ])
    self.assertEqual(p.sieve(10), [ 0, 0, 2, 3, 0, 5, 0, 7, 0, 0, 0 ])
    self.assertEqual(p.sieve(10), [ 0, 0, 2, 3, 0, 5, 0, 7, 0, 0, 0 ])
    self.assertEqual(p.sieve(6), [ 0, 0, 2, 3, 0, 5, 0 ])
    self.assertEqual(p.sieve(5), [ 0, 0, 2, 3, 0, 5 ])
    self.assertEqual(p.sieve(4), [ 0, 0, 2, 3, 0 ])
    self.assertEqual(p.sieve(3), [ 0, 0, 2, 3 ])
    self.assertEqual(p.sieve(2), [ 0, 0, 2 ])
    self.assertEqual(p.sieve(1), [ 0, 0 ])
    self.assertEqual(p.sieve(0), [ 0 ])

  def testIsPrime(self):
    p = primes.Primes()

    self.assertFalse(p.is_prime(0))
    self.assertFalse(p.is_prime(1))
    self.assertFalse(p.is_prime(4))
    self.assertFalse(p.is_prime(100))

    self.assertTrue(p.is_prime(5))
    self.assertTrue(p.is_prime(2))
    self.assertTrue(p.is_prime(3))
    self.assertTrue(p.is_prime(97))

  def testGetMax(self):
    p = primes.Primes(1024)
    self.assertTrue(p.get_max(), 1024)
  
  def testPrimeMask(self):
    p = primes.Primes()
    self.assertEqual(p.prime_mask([ 10, 20, 30, 40, 50 ]), [ 30, 40 ])
    self.assertEqual(p.prime_mask([ 10, 20, 30, 40, 50, 60, 70 ]), [ 30, 40, 60 ])
    self.assertEqual(p.prime_mask([ 10, 20, 30, 40 ]), [ 30, 40 ])
  

if __name__ == "__main__":
  unittest.main()
