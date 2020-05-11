"""
Description:

Task
You are at position [0, 0] in maze NxN and you can only move in one of the four cardinal directions (i.e. North, East, South, West). Return the minimal number of steps to exit position [N-1, N-1] if it is possible to reach the exit from the starting position. Otherwise, return false in JavaScript/Python and -1 in C++/C#/Java.

Empty positions are marked .. Walls are marked W. Start and exit positions are guaranteed to be empty in all test cases.

Path Finder Series:
#1: can you reach the exit?
#2: shortest path
#3: the Alpinist
#4: where are you?
#5: there's someone here
"""

sol = []
maze_size = 0
def path_finder(maze):
  print(maze)
  maze = [list(r) for r in maze.split('\n')]
  global maze_size
  maze_size = len(maze)
  if maze[maze_size-1][maze_size-2] == 'W' and maze[maze_size-2][maze_size-1] == 'W':
    return False
  global sol
  sol = [[ 0 for c in range(maze_size)] for r in range(maze_size)]
  solve_maze(maze, 0, 0)
  num_steps = sum(sum(r) for r in sol)
  if num_steps== 0:
    return False
  else:
    return num_steps - 1

def is_safe(maze, r, c):
  if r >=0 and r<maze_size and c>=0 and c<maze_size and maze[r][c]=='.' and sol[r][c]==0:
    return True
  return False

def solve_maze(maze, r, c):
  if r==maze_size-1 and c==maze_size-1 and maze[r][c]=='.':
    sol[r][c] = 1
    return True
  if is_safe(maze, r, c) == True:
    sol[r][c] = 1
    if solve_maze(maze, r+1, c) == True:
      return True
    if solve_maze(maze, r, c+1) == True:
      return True
    if solve_maze(maze, r-1, c) == True:
      return True
    if solve_maze(maze, r, c-1) == True:
      return True
    sol[r][c] = 0
    return False

"""
Unit Test
"""
from test import Test

a = "\n".join([
  ".W.",
  ".W.",
  "..."
])

b = "\n".join([
  ".W.",
  ".W.",
  "W.."
])

c = "\n".join([
  "......",
  "......",
  "......",
  "......",
  "......",
  "......"
])

d = "\n".join([
  "......",
  "......",
  "......",
  "......",
  ".....W",
  "....W."
])

e = "\n".join([
  ".W...",
  ".W...",
  ".W.W.",
  "...W.",
  "...W."
])

f = "\n".join([
  ".W...",
  "W....",
  ".....",
  ".....",
  "....."
])

Test.assert_equals(path_finder(a), 4)
Test.assert_equals(path_finder(b), False)
Test.assert_equals(path_finder(c), 10)
Test.assert_equals(path_finder(d), False)
Test.assert_equals(path_finder(e), 12)
Test.assert_equals(path_finder(f), 14)
