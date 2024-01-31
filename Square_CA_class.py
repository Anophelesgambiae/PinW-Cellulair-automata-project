
import numpy as np
import matplotlib.pyplot as plot

from CA_class import CA

'''
The square class are the CA classes with square as cells. 
There exists the one-dimensional and two-dimensional square CA (and of course more).

All square CA have a length and a boundary condition. 
These are the different boundary conditions:
- periodic
- constant

The classes under the square classes use the display_CA method.

'''
class square_CA(CA):

    def __init__(self, length: int, boundary_condition: str):
        self.length = length
        self.boundary_condition = boundary_condition

    def display_CA(self, field):
        plot.imshow(field, cmap='binary')
        plot.show()    
