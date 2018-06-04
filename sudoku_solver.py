"""Suduko (9x9) solver using numpy array as input. 

This module contains the following functions:
    
1. Find the next value in the 9x9 that is blank (input as zero).

2. Loop through values 1 to 9. First value that is a valid choice for this cell
   is replaces the incumbent choice.
   
3. Assuming this choice is a permanent choice, loop through and identify if
   there is any solution available with the chosen value. Proceeding as
   such causes loops within loops until finally a solution is found. 

nextval -- Find the next empty value in our array.

val_ok -- Identifes if val is a valid choice according to sudoku logic.

solve -- Runs the algorithm to solve the sudoku.

round_down -- used to find the nearest corner of each square.
"""

import numpy as np

test = np.array([[5,3,0,0,7,0,0,0,0],[6,0,0,1,9,5,0,0,0],[0,9,8,0,0,0,0,6,0],
                 [8,0,0,0,6,0,0,0,3],[4,0,0,8,0,3,0,0,1],[7,0,0,0,2,0,0,0,6],
                 [0,6,0,0,0,0,2,8,0],[0,0,0,4,1,9,0,0,5],[0,0,0,0,8,0,0,7,9]])


def round_down(num, divisor):
    return num - (num%divisor) 


def nextval(sud):
    """Finds the (x,y) co-ordinates of the next zero in the sudoku."""
    for x in range(0,9):
        for y in range(0,9):
            if sud[x,y] == 0:
                return x,y
    return -1, -1


def val_ok(sud, i, j, val):
        """Return True if val is a valid integer for cell (i,j) in sud.
        
        Check row, column, and subgrid criteria. If all are True then return
        True, else False.
        """
        
        row = all(sud[i,s] != val for s in range(0,9))
        if row:
            
            col = all(sud[t,j] != val for t in range(0,9))
            if col:
                # For i,j in subgrid h, find minimum row and column of h.
                # That is, find top-left corner of subgrid.
                min_x = round_down(i,3) 
                min_y = round_down(j,3)
                k = [] # Initialise subgrid list.
                for x in range(0,9):
                    for y in range(0,9):
                        if (x >= min_x and x <= min_x + 2 and 
                            y >= min_y and y <= min_y + 2):
                            # k is distinct list of integers in subgrid.
                            k.append(sud[x][y])                           
                if val not in k:
                    return True 
        return False 
                    
                      
def solve(sud, i=0, j=0):
        """Input sudoku and return a completed sudoku 
        
        Function uses recursion logic to converge to a solution
        """
        (i,j) = nextval(sud)
        if i == -1: # If all values are filled, i.e the sudoku is complete
            return True
        
        for val in range(1,10): 
            if val_ok(sud, i, j, val):
                sud[i][j] = val  
                
                # We find our first value to impute into the suduko. We then 
                # start the loop again given that value.
                if solve(sud, i, j):
                    return True
                else:
                    sud[i][j] = 0
        return False
                  



