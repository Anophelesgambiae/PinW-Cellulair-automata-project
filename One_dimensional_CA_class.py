import numpy as np
from Square_CA_class import square_CA
# Create a class for a one dimensional field
class one_dimension_CA(square_CA):
    def __init__(self,length) -> None:
        # Initialise the field as an array of zeros
        self.field = np.zeros((length), dtype = int)
        # Set the value to 1 for some of the elements on the field
        for column in range(0,len(self.field)):
            self.field[column] = np.random.choice(np.arange(0,2), p=[0.9,0.1])
    # Return a string of the field
    def __str__(self):
        return str(self.field)