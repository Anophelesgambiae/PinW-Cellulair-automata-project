
import numpy as np
from Square_CA_class import square_CA
import msvcrt as ms
import time
import copy

class two_dimension_CA(square_CA):

    # Constructor of the field.
    def __init__(self, length, width):
        # Dimensions of the field.
        self.width = width

        # Initialise the field as an array of zeros
        self.field = np.zeros((length, width), dtype = int)

        # Set the value to 1 for some of the elements on the field
        for row in range(0, len(self.field)):
            for column in range(0 ,len(self.field[row])):
                # The p is a list with the frequency of each state in order of 0 and higher. 
                state = np.random.choice(np.arange(0,2), p=[0.6, 0.4])
                self.field[row][column] = state
        # Remove later
        print(self.field)
        self.next_generation()
    
    # Return a string of the field.
    def __str__(self):
        return str(self.field)    
    
    def next_generation(self):

        while True:
            time.sleep(1)
            old_field = copy.deepcopy(self.field)
            
            # Game of life
            for row in range(1, len(old_field)-1):
                for column in range(1 , len(old_field[row])-1):

                    old_state = old_field[row][column]

                    neighbour_sum = self.return_neighbour_sum(old_field, row, column, None)
                    self.set_new_state(old_state, row, column, neighbour_sum)         

            # Remove later
            print(self.field)

            if ms.kbhit():
                if ord(ms.getch()) == 32:
                    break 
    
    def return_neighbour_sum(self, old_field, row,column, neighbourhood_type):
        neighbour_sum = 0
        for neighbour_row in range(row-1, row+2):
            for neighbour_column in range(column-1, column+2):
                neighbour_sum += old_field[neighbour_row][neighbour_column]
        return neighbour_sum
    
    # Set the new state of the elements not on the boundary.
    def set_new_state(self, old_state, row, column, neighbour_sum):
        if old_state == 1:
            if neighbour_sum < 2:
                new_state = 0
            elif neighbour_sum > 3:
                new_state = 0
            else: new_state = old_state        
        elif old_state == 0 and neighbour_sum == 3:
            new_state = 1
        else: new_state = old_state 

        self.field[row][column] = new_state    

    # We must do something special with the elements on the boundary line. 
    def set_new_state_at_boundary(self, old_state, row, column, neighbour_sum, boundary_condition):
        None

# Test
a = two_dimension_CA(8 ,20)
print(a)