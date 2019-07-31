#!/usr/bin/env python2

__author__ = "marked@gmail.com (Mark Rosetta)"
__version__ = "1.0"

import sys
import math

import bit
import vector
import primes
import pascal

class PrimeBits:
  def __init__(self, bits=64, prefilter=False):
    self.prefilter = prefilter
    self.primes = primes.Primes(bits)
    self.pascal = pascal.Pascal(bits)
  
  def dist_get_cache(self, r):
    """ For values of form 2**r-1, returns dist(2**r-1) from precomputed memory cache. """
    return self.pascal.get_row(r)

  def dist(self, b, a=0):
    """ Returns list with distribution of numbers between a to b, """
    """ by number of bits in binary representation                """
    """ (optionally filtered by primality of sum of 1 bits).      """
    if (b < a or b < 0 or a < 0):
      raise Exception

    result = [ ]
    prev_bits = 0
    if a > 0:
      #TODO : optimizable by removing common bits
      return vector.minus( self.dist(b), self.dist(a-1) )
    else:
      bl = bit.list(b)
      l = len(bl)
      for i, bt in zip(range(l, 0, -1), bl) + [(1, 1)]:
        if bt:
          additional = vector.shift(self.dist_get_cache(i-1), prev_bits)
          if self.prefilter:
            additional = self.primes.prime_mask(additional)
          result = vector.add(result, additional)        
          prev_bits += 1
      return result

  def prime_bits(self, a, b):
    """ Returns the number of values between a and b inclusive for which """
    """ binary representation of value is prime.                         """
    if (b < a or b < 0 or a < 0):
      raise Exception
      
    bit_freq = self.dist(b,a)
    if self.prefilter:
      return sum(bit_freq)
    return sum(self.primes.prime_mask(bit_freq))

if __name__ == "__main__":
  argc = len(sys.argv)
  if argc == 1 or argc % 2 == 0:
    print "Usage: %s A B ..." % (sys.argv[0])
    exit()
  pb = PrimeBits(bits=64, prefilter=True)
  for i in range(1,argc,2):
    A = eval(sys.argv[i])
    B = eval(sys.argv[i+1])
    print A, "-", B, ":", pb.prime_bits(A, B)  
