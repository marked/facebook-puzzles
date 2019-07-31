#!/usr/bin/env python2

__author__ = "marked@gmail.com (Mark Rosetta)"
__version__ = "1.0"

import math

def width(n):
  """ width() returns # of bits needed to represent input """
  if n == 0:
    return 1
  return int(1+math.log(n,2))

def list(n):
  """ list() returns bit represention of input in a list """
  if n == 0:
    return [0]
  bl = []
  while n != 0:
    bl.append(n & 1)
    n >>= 1
  bl.reverse()
  return bl
