# -*- coding: utf-8 -*-
"""
Created on Sun Nov  2 17:27:52 2025

@author: henri
"""

import random

def create_grid(num_rows, num_cols):
    """ creates and returns a 2-D list of 0s with the specified dimensions.
        inputs: num_rows and num_cols are non-negative integers
    """
    grid = []
    
    for r in range(num_rows):
        row = [0] * num_cols     # a row containing width 0s
        grid += [row]

    return grid

def print_grid(grid):
    """ prints the 2-D list specified by grid in 2-D form,
        with each row on its own line.
        input: grid is a 2-D list
    """
    num_rows = len(grid)
    for r in range(num_rows):
        if r == 0:
            print('[', end='')
        else:
            print(' ', end='')
        if r < num_rows - 1:
            print(str(grid[r]) + ',')
        else:
            print(str(grid[r]) + ']')

def random_grid(num_rows, num_cols):
    """ creates and returns a 2-D list with the specified dimensions
        in which each cell is assigned a random integer from 0-9.
        inputs: num_rows and num_cols are non-negative integers
    """
    grid = create_grid(num_rows, num_cols)

    for r in range(num_rows):
        for c in range(num_cols):
            grid[r][c] = random.choice(range(10))
            
    return grid

# function 1
def col_index_grid(num_rows, num_cols):
    """creates and return a 2-D list of given size where each cell equals its column index."""
    grid = create_grid(num_rows, num_cols)
    
    for r in range(num_rows):
        for c in range(num_cols):
            grid[r][c] = c
            
    return grid

# function 2
def num_between(grid, n1, n2):
    """return how many grid values lie between n1 and n2."""
    count = 0
    for r in range(len(grid)):
        for c in range(len(grid[0])):
            if grid[r][c] <= n2 and grid[r][c] >= n1:
                count += 1
    
    return count

# function 3
def copy(grid):
    """ returns a deep copy of grid (new 2-D list with same shape and values)."""
    new_grid = create_grid(len(grid), len(grid[0]))
    
    for r in range(len(grid)):
        for c in range(len(grid[0])):
            new_grid[r][c] = grid[r][c]
    
    return new_grid

# function 4
def double_with_cap(grid, cap):
    """double each cell; if it would exceed cap, set it to cap."""
    for r in range(len(grid)):
        for c in range(len(grid[0])):
            if grid[r][c] * 2 > cap:
                grid[r][c] = cap
            else:
                grid[r][c] *= 2

# function 5
def sum_evens_in_col(grid, colnum):
    """computes and return the sum of even numbers in column colnum."""
    sum_even = 0
    
    for r in range(len(grid)):
        if grid[r][colnum] % 2 == 0:
            sum_even += grid[r][colnum]
    
    return sum_even
