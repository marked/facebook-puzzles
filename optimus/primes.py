#!/usr/bin/env python2

__author__ = "marked@gmail.com (Mark Rosetta)"
__version__ = "1.0"

import math

class Primes:
  def __init__(self, seed=0):
    self.cache = [ 0 ]
    self.max_cache = 0
    self.sieve(seed)
    
  def sieve(self, n):
    if n <= self.max_cache:
      return self.cache[:n+1]
    table = range(1+n)
    table[1] = 0
    for i in range(1,1+int(math.ceil(math.sqrt(n)))):
      if table[i]:
        for j in range(i**2,n+1,i):
          table[j] = 0
    self.cache = table
    self.max_cache = n
    return self.cache[:]

  def is_prime(self, n):
    if ( n <= self.max_cache ):
      return self.cache[n] > 0
    else:
      self.sieve(n)
      return self.cache[n] > 0
      
  def get_max(self):
    return self.max_cache
  
  def prime_mask(self, v):
#    return filter(lambda x, y: x*self.is_prime(y), v, v)
    result = []
    self.sieve(len(v))
    for p in self.cache[:len(v)]:
      if p:
        result.append(v[p])
    return result