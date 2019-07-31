#!/usr/bin/env python2

__author__ = "marked@gmail.com (Mark Rosetta)"
__version__ = "1.0"

""" Unit test for gambling.py """

import gambling
import unittest

class GamblingTestCase(unittest.TestCase):
  def testToyProblem(self):
    toy_adj = [ 
      [ 1, 1, 0 ],
      [ 1, 1, 1 ],
      [ 0, 1, 1 ]
    ]

    toy_wins = [
      [ -22, -63, -78,  75 ],
      [ -85,  50,  24, -63 ],
      [  77,  53, -86, -25 ],
    ]

    cp = gambling.CasinoPath(toy_adj, toy_wins)

    self.assertEqual(cp.generate_paths(), [[1, 2, 2], [1, 1, 1], [0, 0, 'H'], ['H', 'H', 'H']])
    self.assertEqual(cp.find_best_start(0), (1, 1))
    self.assertEqual(cp.print_path_from( (1, 1) ), [ 1, 1, 0 ])
    
    self.assertEqual(cp.invert_matrix(toy_wins), [[-22, -85, 77], [-63, 50, 53], [-78, 24, -86], [75, -63, -25]])
    self.assertEqual(cp.edge2node(toy_adj), [[0, 1], [0, 1, 2], [1, 2]])
    
if __name__ == "__main__":
  unittest.main()
