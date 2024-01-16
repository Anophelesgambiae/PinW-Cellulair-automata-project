
import numpy as np
from Square_CA_class import square_CA
import msvcrt as ms
import time
import copy

'''
This a class of a two dimensional Cellulair automata (CA). The field is thus a retangle with a predefined length and width.  
'''
class two_dimension_CA(square_CA):

    # Constructor of the field.
    def __init__(self, length, width, neighbourhood_rule, boundary_condition):
        # Dimensions of the field.
        self.width = width
        self.neighbourhood_rule = neighbourhood_rule

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
        self.next_generation(neighbourhood_rule, boundary_condition)
    
    # Return a string of the field.
    def __str__(self):
        return str(self.field)    
    
    def next_generation(self, neighbourhood_rule, boundary_condition):

        while True:
            time.sleep(1)
            old_field = copy.deepcopy(self.field)
            
            match boundary_condition:
                case "periodic":
                    for row in range(0, len(old_field)):
                        for column in range(0 , len(old_field[row])):

                            old_state = old_field[row][column]

                            neighbour_sum = self.return_neighbour_sum(old_field, row, column, neighbourhood_rule)
                            self.set_new_state(old_state, row, column, neighbour_sum)   

                case "constant":
                    for row in range(1, len(old_field)-1):
                        for column in range(1 , len(old_field[row])-1):

                            old_state = old_field[row][column]

                            neighbour_sum = self.return_neighbour_sum(old_field, row, column, neighbourhood_rule)
                            self.set_new_state(old_state, row, column, neighbour_sum) 

            # Remove later
            print(self.field)

            if ms.kbhit():
                if ord(ms.getch()) == 32:
                    break 
    '''

    '''
    def return_neighbour_sum(self, old_field, row, column, neighbourhood_rule):
        match neighbourhood_rule:
            case "Moore":
                    neighbour_sum = old_field[(row-1) % (len(old_field))][(column-1) % (len(old_field[row]))] + \
                                    old_field[(row-1) % (len(old_field))][column] + \
                                    old_field[(row-1) % (len(old_field))][(column+1) % (len(old_field[row]))] + \
                                    old_field[row][(column-1) % (len(old_field[row]))] + \
                                    old_field[row][(column+1) % (len(old_field[row]))] + \
                                    old_field[(row+1) % (len(old_field))][(column-1) % (len(old_field[row]))] + \
                                    old_field[(row+1) % (len(old_field))][column] + \
                                    old_field[(row+1) % (len(old_field))][(column+1) % (len(old_field[row]))]
            case "vonNeumann":
                    neighbour_sum = old_field[(row-2) % (len(old_field))][column] + \
                                    old_field[(row-1) % (len(old_field))][column] + \
                                    old_field[row][(column-2) % (len(old_field[row]))] + \
                                    old_field[row][(column-1) % (len(old_field[row]))] + \
                                    old_field[row][(column+1) % (len(old_field[row]))] + \
                                    old_field[row][(column+2) % (len(old_field[row]))] + \
                                    old_field[(row-1) % (len(old_field))][column] + \
                                    old_field[(row-2) % (len(old_field))][column] 

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

    

# Test
a = two_dimension_CA(8, 20, "Moore", "constant")
print(a)