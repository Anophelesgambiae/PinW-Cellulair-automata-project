import numpy as np
import time
import copy
import msvcrt as ms
from Square_CA_class import square_CA

# Create a class for a one dimensional field
class one_dimension_CA(square_CA):

    # Create a field initializer
    def __init__(self,length,boundary_condition) -> None:

        # Initialise the field as an array of zeros
        self.field = np.zeros(length, dtype = int)

        # Set the value to 1 for some of the elements on the field
        self.field[(length//2)] = 1
        # for column in range(0, len(self.field)):
            # self.field[column] = np.random.choice(np.arange(0, 2), p = [0.5, 0.5])
        print(self.field)
        self.Next_generation(length,boundary_condition)

    # Define how the next generation is created
    def Next_generation(self,length,):
        while True:
            time.sleep(1)
            rule_30 = {"111":0, "110":0, "101":0, "100":1, "011":1, "010":1, "001":1, "000":0}
            old_field = copy.deepcopy(self.field)
            match boundary_condition:
                case "periodic":
                    for column in range(0, len(self.field)):
                        newstate = rule_30[str(old_field[(column-1) % len(old_field)])
                                           + str(old_field[column])
                                           + str(old_field[(column+1) % len(old_field)])]
                        self.field[column] = newstate
                case "constant":
                    for column in range(1, len(self.field)-1):
                        newstate = rule_30[str(old_field[(column-1)])
                                           + str(old_field[column])
                                           + str(old_field[(column+1)])]
                        self.field[column] = newstate
            print(self.field)
            if ms.kbhit():
                if ord(ms.getch()) == 32:
                    break

    # Return a string of the field
    def __str__(self):
        return str(self.field)
a = one_dimension_CA(31,"constant")        
