
import numpy as np
import msvcrt as ms
import time
import copy
import types
import matplotlib.pyplot as plot

from Square_CA_class import square_CA


'''
This a class of a two dimensional Cellulair automata (CA). 
The field is thus a retangle with a predefined length and width.

The length and width must be an integer.
The rule, neighbourhood_rule and boundary_condition must be a string.

The rule is how we can define when a cell have the state 0 or 1. We have the following rules:
- Life: The rule used for the game of Life CA 

The neighbourhood_rule is what are the neigbours of one cell. The rules are:
- Moore: all horizontal, vertical and diagonal adjacent cells are neighbours.  
- vonNeumann: same as the Moore except the cell on the diagonal are not neighbours. 

The boundary_condition is what we do with the cells at the boundary. The rules are:
- periodic: a borderless field (the borders of the field are connected as a donut)  
- constant: the field have a border (thus the cells on the border are constant)

'''
class two_dimension_CA(square_CA):

    '''
    Make a field with a random state on each cell. Calls the next_generation method.
    '''
    def __init__(self, length: int, width: int, rule: str, neighbourhood_rule: str, 
                 boundary_condition: str, timesteps: int):

        
        self.width: int = width
        self.neighbourhood_rule: str = neighbourhood_rule
        self.rule: str = rule

        # Initialise the field as an array of zeros.
        self.field: np.array = np.zeros((length, width), dtype = int)
        # Set the value to 1 for some of the elements on the field
        for row in range(0, length):
            for column in range(0 , width):
                # The p is a list with the frequency of each state in order of 0 and higher. 
                state: int = np.random.choice(np.arange(0,2), p=[0.5, 0.5])
                self.field[row][column] = state

        self.next_generation(length, width, rule, neighbourhood_rule, boundary_condition, timesteps)
    
    # Return a string of the field.
    def __str__(self) -> str:
        return str(self.field)    
    '''
    Define for all cells on the field the new state (0 or 1). 
    This function runs the given timesteps or stops when the user press space or esc.
    You can define new boundary_condition to make a new case with a new name in a string. 
    In this case you define with a for loop which cells can change.
    '''
    def next_generation(self, length: int, width: int, rule: str, neighbourhood_rule: str, boundary_condition: str, timesteps: int):
        

        for t in range(0, timesteps):
            
            # Stops the run when you press space or esc.
            if ms.kbhit():
                if ord(ms.getch()) in [27,32]:
                    quit()
            
            old_field: np.array = copy.deepcopy(self.field) 
            
            match boundary_condition:
                case "periodic":
                    for row in range(0, length):
                        for column in range(0 , width):

                            self.set_new_state(length, width, old_field, row, column, rule, neighbourhood_rule)   

                case "constant":
                    for row in range(1, length-1):
                        for column in range(1 , width-1):

                            self.set_new_state(length, width, old_field, row, column, rule, neighbourhood_rule)

                case _:
                    print("NameError: " + str(boundary_condition) + 
                          "is not defined in the next_generation method, perhaps you made a typo" )
                    quit()

        print("CA has done " + str(timesteps) + " timesteps") 
        super().display_CA(self.field)
                            
    '''
    Set the new state (0 or 1) of the cel on the given row and column. 
    With the game of life the following rules exists:
    - a living cell dies when there are less than 2 living cells in their neighbourhood (underpopulation).
    - a living cell dies when there are more than 3 living cells in their neighbourhood (overpopulation).
    - a living cell lives otherwise.
    - a dead cell will be born when there exactly 3 living cells in their neighbourhood (reproduction)

    You can define new rules to make a new case with a new name in a string. With if statements you can tell when living cells die
    and when dead cells born. 
    '''
    def set_new_state(self, length: int, width: int, old_field: np.array, row: int, column: int, rule: str, neighbourhood_rule: str):

        old_state = old_field[row][column]

        neighbour_sum = self.return_neighbour_sum(length, width, old_field, row, column, neighbourhood_rule)

        match rule:
            case "Life":
                if old_state == 1:
                    if neighbour_sum < 2:
                        new_state = 0
                    elif neighbour_sum > 3:
                        new_state = 0
                    else: new_state = old_state        
                elif old_state == 0 and neighbour_sum == 3:
                    new_state = 1
                else: new_state = old_state 

            case _:
                print("NameError: " + str(rule) + \
                      "is not defined in the set_new_state method, perhaps you made a typo" )
                quit()    

        self.field[row][column] = new_state    

    '''
    Calculates the number of living cells in the neighbourhood.

    You can define new rules to make a new case with a new name in a string. You can define which cells are calculated.
    Example: old_field[3][5] returns the state of a cell on row 3 and column 5. 
    '''
    def return_neighbour_sum(self, length: int, width: int, old_field: np.array, row: int, column: int, neighbourhood_rule: str) -> int:
        match neighbourhood_rule:
            case "Moore":
                    neighbour_sum = old_field[(row-1) % length][(column-1) % width] + \
                                    old_field[(row-1) % length][column] + \
                                    old_field[(row-1) % length][(column+1) % width] + \
                                    old_field[row][(column-1) % width] + \
                                    old_field[row][(column+1) % width] + \
                                    old_field[(row+1) % length][(column-1) % width] + \
                                    old_field[(row+1) % length][column] + \
                                    old_field[(row+1) % length][(column+1) % width]
            case "vonNeumann":
                    neighbour_sum = old_field[(row-1) % length][column] + \
                                    old_field[row][(column-1) % width] + \
                                    old_field[row][(column+1) % width] + \
                                    old_field[(row+1) % length][column] 
            case _:
                print("NameError: " + str(neighbourhood_rule) + \
                      "is not defined in the return_neighbour_sum method, perhaps you made a typo" )
                quit()

        return neighbour_sum


# Make a two dimensional CA with the inputs of the user.
dimensions: list[str] = input("What is the length and width of the CA? ").split(" ")

try:
    length: int = int(dimensions[0])
except ValueError:
    print("TypeError: length must be an integer")
    quit()     

try:
    width: int = int(dimensions[1])
except ValueError:
    print("TypeError: width must be an integer")
    quit()        

if length < 3 or length > 1000:
    print("ValueError: length must be between 3 and 1000, your length was " + str(length))
    quit()

if width < 3 or width > 1000:
    print("ValueError: width must be between 3 and 1000, your width was " + str(width))
    quit()    

rules: list[str] = input("What is the rule, neighbourhood rule and boundary condition?: ").split(" ")

rule: str = rules[0]
neighbourhood_rule: str = rules[1]
boundary_condition: str = rules[2]

try:    
    timesteps: int = int(input("How many timesteps you want that the CA runs: ") )
except ValueError:
    print("TypeError: timesteps must be a integer")
    quit()

if timesteps < 0 or timesteps > 1000:
    print("ValueError: timesteps must be between 0 and 1000, your timesteps was " + str(timesteps))    

CA = two_dimension_CA(length, width, rule, neighbourhood_rule, boundary_condition, timesteps)




