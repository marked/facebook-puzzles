#!/usr/bin/env python

__author__ = "marked@gmail.com (Mark Rosetta)"
__version__ = "1.0"

def add(v1, v2):
  l = min(len(v1), len(v2))
  return map(lambda x, y: x+y, v1[:l], v2[:l]) + v1[l:] + v2 [l:]

def minus(v1, v2):
  l = max(len(v1), len(v2))
  return map(lambda x, y: x-y, v1+[0]*(l-len(v1)),v2+[0]*(l-len(v2)) )

def shift(v1, offset):
  return [0]*offset + v1
