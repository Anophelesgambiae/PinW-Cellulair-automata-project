
import numpy as np
from CA_class import CA

'''
The square class are the CA classes with square as cells. 
There exists the one-dimensional and two-dimensional square CA (and of course more).
All square CA have a length and a boundary condition. 
'''
class square_CA(CA):

    def __init__(self, length, boundary_condition):
        self.length = length
        self.boundary_condition = boundary_condition