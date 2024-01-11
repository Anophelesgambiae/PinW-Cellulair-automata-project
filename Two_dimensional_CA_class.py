
import numpy as np
from Square_CA_class import square_CA

class two_dimension_CA(square_CA):

    # Constructor of the field.
    def __init__(self, length, width):
        # Dimensions of the field.
        self.width = width

        # Initialise the field with only state 0.
        self.field = np.zeros((length, width), dtype = int)
        self.timestep = 0
        # Populate the field with some other states.
        for row in range(0, len(self.field)):
            for column in range(0 ,len(self.field[row])):
                # The p is a list with the frequency of each state in order of 0 and higher. 
                state = np.random.choice(np.arange(0,2), p=[0.8, 0.2])
                self.field[row][column] = state

    def __str__(self):
        return str(self.field)    

    def Next_generation():


a = two_dimension_CA(2,8,20)
print(a)