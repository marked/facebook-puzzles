#!/usr/bin/env python

__author__ = "marked@gmail.com (Mark Rosetta)"
__version__ = "1.0"

""" Finds optimal paths through 2d map cross time where each coordinate has an associated score. """

class CasinoPath:
  def __init__(self, adj, wins):
    self.adj = self.edge2node(adj)
    self.wins = self.invert_matrix(wins)
    self.best_moves = None
    self.best_wins = None
    
  def generate_paths(self):
    """ For all space-time coordinates as starting positions, calculates         """
    """ optimal path from that point forward along with expected future winnings """
    """ by starting from there / then.                                           """

    wins = self.wins
    
    num_days = len(self.wins)
    num_casinos = len(self.adj)

    best_moves =  [ [None]*num_casinos for i in range(num_days) ]
    best_wins  =  [ [None]*num_casinos for i in range(num_days) ]

    for day in range(num_days-1,0-1,-1):
      if day == num_days-1:
        # last day
        best_wins[day] = wins[day][:]
        best_moves[day] = ['H'] * num_casinos
      else:
        # not last day
        for cur_casino in range(0, num_casinos):
          today_wins = wins[day][cur_casino]
          actions = { 0: "H" }
          for next_casino in self.neighbors(cur_casino):
            actions[best_wins[day+1][next_casino]] = next_casino
          move_to_make = max(actions.keys())  
          best_moves[day][cur_casino] = actions[move_to_make]
          best_wins[day][cur_casino] = wins[day][cur_casino] + move_to_make
    self.best_wins = best_wins
    self.best_moves =  best_moves
    return best_moves

  def find_best_start(self, start_place):
    """ Given generated optimal paths, finds ideal delayed starting point. """
    """ following constraint of reachability from actual starting point.   """
    
    start_place = start_place
    num_days = len(self.wins)
    num_casinos = len(self.adj)

    reachable = range(num_days)
    neighborhood = set()

    neighborhood.add(start_place)

    for day in range(num_days):
      reachable[day] = neighborhood.copy()
      for start_place in reachable[day]:
        neighborhood.update(set(self.neighbors(start_place)))

    best_start_casino = 'H'
    best_start_day = 0
    best_start_wins = 0
    for day in range(num_days):
      for casino in reachable[day]:
        if self.best_wins[day][casino] > best_start_wins:
          best_start_casino = casino
          best_start_day = day
          best_start_wins = self.best_wins[day][casino]
    return (best_start_day, best_start_casino)

  def print_path_from(self, start):
    """ Prints previously generated optimal path from start postion. """
    start_day = start[0]
    start_place = start[1]

    path = [ ]    
    d = start_day
    p = start_place
    while (p != 'H'):
      print "Day: ", d, "\tCasino: ", p, "\tWin: ", self.wins[d][p]
      path.append(p)
      p = self.best_moves[d][p]
      d+=1
    print "Go home with $", self.best_wins[start_day][start_place]
    return path

  def neighbors(self, start):
    return self.adj[start]
    
  def edge2node(self, edge_matrix):
    """ Converts edge based adjacency matrix to node based. """
    node_matrix = [ ]
    for edge_row in edge_matrix:
      node_matrix.append (
        filter(lambda x: edge_row[x], range(len(edge_row)))
      )
    return node_matrix
    
  def invert_matrix(self, old_matrix):
    """ Inverts matrix (from row major to column major / vice-versa). """
    old_height = len(old_matrix)
    old_width = len(old_matrix[0])    
    new_matrix =  [ [None]*old_height for i in range(old_width) ]
    for i in range(old_height):
      for j in range(old_width):
        new_matrix[j][i] = old_matrix[i][j]
    return new_matrix

if __name__ == "__main__":
  fb_adj = [
    [1, 1, 0, 1, 0, 0, 0, 0, 0],
    [1, 1, 1, 0, 1, 0, 0, 0, 0],
    [0, 1, 1, 0, 0, 1, 0, 0, 0],
    [1, 0, 0, 1, 1, 0, 1, 0, 0],
    [0, 1, 0, 1, 1, 1, 0, 1, 0],
    [0, 0, 1, 0, 1, 1, 0, 0, 1],
    [0, 0, 0, 1, 0, 0, 1, 1, 0],
    [0, 0, 0, 0, 1, 0, 1, 1, 1],
    [0, 0, 0, 0, 0, 1, 0, 1, 1]
  ]

  fb_wins = [
    [ 53,-84, 50,-73, 54, 60, 74, 22,-63,-78, 75, 72,
         -46, 99,-33, 24,  6,-66, 77,-61,-60,-46,-52, 84,
          91,-21,-52,-72,-39,-41],
    [ 77,-86,-25, 27,-59,-71,-13,-85, 50, 24,-63, 26,
          -4,-10, 25, 62,-85,-68, 96, 92,-29,-64,-54, 18,
         -79,-62, 97,-32,-35,-42],
    [ 27,-57,-28,-98, 69, 12,-70,-43, 27, 80, 80, 64,
           6,-23,-45,-68,-60,-31,-36,-63,-39, 34,-27,  7,
         -47, -7, 44,-50, 60,-90],
    [  7,-12,-48, 79,-11,-78, -8, 19,-21,-81, -1,-40,
          83,-95, 36,-62,-63, 76,  6,  0,-87, 67,-66,-15,
         -26,-14, 78,-81, 36, 38],
    [-71,-56,-73,-20,-77, 15,  2, 14,-66, 81, 33, 33,
         -59, 16, 37, 77, 53, 73, 53,-40,-26, 66,-73,  7,
         -48,  1, 93,-70, 19, 30],
    [ 68, 47, 73, 94,-72, 96, 10, 30, 11, 44, 11,-56,
         -23, 51, 60,-86, 29, 13, 87,-17, 73,-39,-51,-99,
          68,  1,  1, 62, 30,-79],
    [ -8, -1, 68,-34, -7, 96,-37,-96, 26, 73, 47,-62,
         -83,-76, 89, 77,-62, 18, -9,-75,-99,-36,-14,-50,
         -36,-45, 50, 64,-83,-19],
    [ 85,  9, 79, 53, 75,-28, 49,-62,-25,-24,-89,-77,
          13,-72,-54,  2,-95,-17,-80, -5,  8,-79, 59, 93,
         -30,-77,-51,-79, 87,-35],
    [  1, 72, 74,-20, 26, 49, 52,-25, 86,-72, 50, 97,
         -50,-36,-74, -4, 65,-70, 78, 85, 25,-14,-93,-16,
         -20,-24,  7, 28, -3, -5]
  ]
  
  cp = CasinoPath(fb_adj, fb_wins)
  cp.generate_paths()
  cp.print_path_from( cp.find_best_start(0) )
