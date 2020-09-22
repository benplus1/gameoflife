## Game of Life

## Using a 2D array for datastructure

## class Game <-- delete
## -- init: grid object, is a 2D array
## grid.update()
## -- step_forward: takes in user input
## -- print_game: delay second between prints

## class Grid
# [[0,0,1,]]
## -- update: 3 rules - loneliness, overpopulation, reproduction

## rowNbr = [-1, -1, -1,  0, 0,  1, 1, 1]; 
            # colNbr = [-1,  0,  1, -1, 1, -1, 0, 1]; 

        # Recur for all connected neighbours 
        # for k in range(8): 
        #     if self.isSafe(i + rowNbr[k], j + colNbr[k], visited): 
        #         self.DFS(i + rowNbr[k], j + colNbr[k], visited) 
##


import copy
import time

class Game(object):
  def __init__(self):
    self.grid = Grid(10)

  def step_forward(self):
    # Given input, run that many steps. Ends program if given STOP commnd
    input_steps = int(input("How long would you like to run the game of life for: "))

    for step in range(input_steps):
      self.grid.update()
      self.grid.print_grid()
      time.sleep(1)

class Grid(object):
  def __init__(self, grid_size):
    # self.matrix = [[0 for i in range(grid_size)] for i in range(grid_size)]
    # self.matrix = [[0,1,1,],[1,1,1], [0,0,0]]
    self.matrix = [[0,1,1,1],[1,1,1,1], [0,0,0,0], [1,1,1,1]]

  def update(self):
    temp_grid = copy.deepcopy(self.matrix)
    

    rowNbr = [-1, -1, -1,  0, 0,  1, 1, 1]; 
    colNbr = [-1,  0,  1, -1, 1, -1, 0, 1]; 
    
    for row, rowlist in enumerate(self.matrix):
      for col in range(len(rowlist)):
        num_neighbors = 0
        # if self.matrix[row][col] == 0:
        #   continue
        current_cell = self.matrix[row][col]

        # Pull neighbors
        for k in range(8): 
            if (row + rowNbr[k]) < 0 or (row + rowNbr[k]) >= len(self.matrix):
              continue
            if (col + colNbr[k]) < 0 or (col + colNbr[k]) >= len(self.matrix):
              continue
            if self.matrix[row + rowNbr[k]][col + colNbr[k]] == 1: 
              num_neighbors += 1
        
        # Reproduction
        if current_cell == 0 and num_neighbors == 3:
          temp_grid[row][col] = 1
        
        # Overpopulation or Loneliness
        if current_cell == 1 and (num_neighbors >= 4 or num_neighbors <= 1):
          temp_grid[row][col] = 0
    
    self.matrix = temp_grid

  def print_grid(self):
    # prints the grid to the command 
    for row, rowlist in enumerate(self.matrix):
      for col in range(len(rowlist)):
        print (f'{self.matrix[row][col]} ', end='')
      print ('')

if __name__ == "__main__":

  # grid = Grid(10)
  # grid.print_grid()
  # grid.update()
  # print('')
  # grid.print_grid()

  game = Game()
  game.step_forward()

  # 101
  # 101
  # 010