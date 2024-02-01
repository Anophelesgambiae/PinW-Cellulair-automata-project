
import numpy as np
import msvcrt as ms
import time
import copy
import types
import json

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

# Give the user some information on how to use the code and help the user
# when they give unusable inputs. 

'''
Controls for the number of elements in a string list.
'''
def control_number_of_elements_in_input(input: list[str], numbers_of_elements: int):
    if len(input) != numbers_of_elements:
        print("Error: you have typed " + str(len(input)) + " elements, but there are " + str(numbers_of_elements) + " needed")
        quit()
    else: None

'''  
Controls if the input has type int.
'''
def control_for_int_type(input: int):
    if str(type(json.loads(input))) != "<class 'int'>":
        print("TypeError: " + str(input) + " is not an integer")
        quit()    
    else: None

'''  
Controls if length is between 3 and 1000.
'''
def control_length_value(length):
    if length < 3 or length > 1000:
        print("ValueError: length must be between 3 and 1000, your length was " + str(length))
        quit()
    else: None

'''  
Controls if rule_number is between 0 and 255.
'''
def control_rule_number_value(rule_number):
    if rule_number < 0 or rule_number > 255:
        print("ValueError: please give an integer between 0 and 255, your rule_number was " + str(rule_number))
        quit()                
    else: None

'''  
Controls if timesteps is between 0 and 1000.
'''
def control_timesteps_value(timesteps):
    if timesteps < 0 or timesteps > 1000:
        print("ValueError: timesteps must be between 0 and 1000, your timesteps was " + str(timesteps))
        quit()
    else: None    

'''  
Construct the CA with the input of the user.
For CA_type you can give as input the '1d_CA' and '2d_CA':
'''
def construct_CA_from_user_input():
    
    print("What should the length and width of the field be? (seperated with a space)")
    print("Please give your inputs as an integer between 3 and 1000.")

    dimensions = input().split(" ")
    control_number_of_elements_in_input(dimensions, 2)

    length_input: str = dimensions[0]
    control_for_int_type(length_input)
    length: int = int(length_input)
    control_length_value(length)
            
    width_input: str = dimensions[1]
    control_for_int_type(width_input)
    width: int = int(width_input)
    control_length_value(width)

    print("")
    print("What rule, neighbour_rule and border_condition do you want to use? (seperated with a space)")
    print("For rule you can choose 'Life'.")
    print("For neighbour_rule you can choose between 'Moore' and 'vonNeumann'")
    print("For border_condition you can choose between 'periodic' and 'constant'.")

    rules = input().split(" ")
    control_number_of_elements_in_input(rules, 3)
            
    rule: str = rules[0]
    neighbourhood_rule: str = rules[1]
    border_condition: str = rules[2]
  
    print("")
    print("How many timesteps do you want to generate?")
    print("Please give your input as an integer between 0 and 1000.")

    timesteps_input: str = input()
    control_number_of_elements_in_input(timesteps_input, 1)
    control_for_int_type(timesteps_input)
    timesteps: int = int(timesteps_input)
    control_timesteps_value(timesteps)

    two_dimension_CA(length, width, rule, neighbourhood_rule, border_condition, timesteps)


construct_CA_from_user_input()