#!/usr/bin/env python

__author__ = "marked@gmail.com (Mark Rosetta)"
__version__ = "1.0"

import vector

class Pascal:      
  def __init__(self, seed=0):
    self.cache = [ [ 1 ] ]
    self.max_cache = 0
    self.extend(seed)

  def extend(self,n):
    if n <= self.max_cache:
      return self.cache[:n+1]
    result = self.cache
    row = self.cache[-1]
    for i in range(self.max_cache,n+1):
      row = vector.add(row, vector.shift(row, 1))
      result.append(row)
    self.cache = result
    self.max_cache = n   
    return result
    
  def get_row(self, n):
    if n <= self.max_cache:
      return self.cache[n]
    else:
      self.extend(n)
      return self.cache[n]
      
  def get_max(self):
    return self.max_cache

if __name__ == "__main__":
  import sys
  if len(sys.argv) == 2:
    max = int(sys.argv[1])
    p = Pascal(max)
    print p.extend(max)
