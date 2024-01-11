
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

        # Initialise the field with only state 0.
        self.field = np.zeros((length, width), dtype = int)

        # Populate the field with some other states.
        for row in range(0, len(self.field)):
            for column in range(0 ,len(self.field[row])):
                # The p is a list with the frequency of each state in order of 0 and higher. 
                state = np.random.choice(np.arange(0,2), p=[0.6, 0.4])
                self.field[row][column] = state
        
        print(self.field)
        self.next_generation()
    
    # Return a string of the field.
    def __str__(self):
        return str(self.field)    
    
    def next_generation(self):

        while True:
            time.sleep(1)
            old_field = copy.deepcopy(self.field)
             
            for row in range(0, len(old_field)):
                for column in range(0 , len(old_field[row])):
                    # Test
                    if old_field[row][column-1] == 0:
                        self.field[row][column] = 0
                    else: self.field[row][column] = 1     

            print(self.field)

            if ms.kbhit():
                if ord(ms.getch()) == 32:
                    break 


a = two_dimension_CA(3,12)
print(a)