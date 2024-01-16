
import numpy as np
from CA_class import CA

class square_CA(CA):

    def __init__(self, length, boundary_condition):
        self.length = length
        self.boundary_condition = boundary_condition