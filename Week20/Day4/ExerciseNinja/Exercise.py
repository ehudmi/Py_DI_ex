# Exercise 1 : Conway’s Game Of Life
# What You Will Create
# Conway's Game of Life


# Instructions
# These are the rules of the Game of Life (as stated in Wikipedia):

# The universe of the Game of Life is an infinite, two-dimensional orthogonal grid of square cells, each of
# which is in one of two possible states, alive or dead, (or populated and unpopulated, respectively).

# Every cell interacts with its eight neighbors, which are the cells that are horizontally, vertically, or
# diagonally adjacent. At each step in time, the following transitions occur:

# Any live cell with fewer than two live neighbors dies, as if by under-population.
# Any live cell with two or three live neighbors lives on to the next generation.
# Any live cell with more than three live neighbors dies, as if by overpopulation.
# Any dead cell with exactly three live neighbors becomes a live cell, as if by reproduction.
# Using these rules, implement the Game. (Hint: use Classes !!!!)
# Use a few different initial states to see how the game ends.

# Notes:

# Display the grid after each generation
# The end of the game is fully determined by the initial state. So have it pass through your program and see how
# it ends.
# Be creative, but use classes
# The game can have fixed borders and can also have moving borders. First implement the fixed borders.
# Each “live” cell that is going out of the border, exits the game.
# Bonus: Make the game with ever expandable borders, make the maximum border size a very large number(10,000)
# so you won’t cause a memory overflow
