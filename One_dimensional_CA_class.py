import numpy as np
import copy
import msvcrt as ms
import matplotlib as plot
import types
import json

from Square_CA_class import square_CA


class one_dimension_CA(square_CA):
    '''
    A class for one dimensional CA's is created.

    The inputs are as follows:
    -length: An integer of the length of the field
    -boundary-condition: "constant" for a system with borders
     and "periodic" for a borderless field
    -rule_number: The rule number used for the CA
    '''

    def __init__(self, length: int, boundary_condition: str,
                 rule_number: int, timesteps: int):
        '''Return the starting field and the dictionary of the CA''' 

        # Create the dictionary for the rule. The input represents the
        # element's neighbour, the element itself and the element's right
        # neighbour
        rule_dict: dict = {"111":0, "110":0, "101":0, "100":0, 
                     "011":0, "010":0, "001":0, "000":0}
        binary_number: str = "{0:08b}".format(rule_number)
        binary_list: list = list(binary_number)
        key_items_list: list = ["111", "110", "101", "100",
                          "011", "010", "001", "000"]
        i = 0
        for key in key_items_list:
            rule_dict[key] = int(binary_list[i])
            i += 1
        self.rule_dict = rule_dict
            
        # Initialize the field where the elements have a 50% chance to be
        # a zero and 50% chance to be a one
        self.field: np.array = np.zeros(length, dtype = int)
        for item in range(0, len(self.field)):
            self.field[item] = np.random.choice(np.arange(0, 2),
                                                p=[0.5, 0.5])
        
        self.Next_generation(length, boundary_condition, rule_dict, timesteps)

    def Next_generation(self, length: int, boundary_condition: str,
                        rule_dict: dict, timesteps: int):
        ''' Return the next generation of the CA '''

        # Store each generation of the CA in the field_history list so that 
        # they can be displayed later
        field_history: list = []
        for t in range(0, timesteps):
            old_field: np.array = copy.deepcopy(self.field)
            field_history.append(old_field)

            match boundary_condition:

                # Create a periodic border by adding %length when looking at
                # the neighbours so that the first element's left neighbour
                # will be the last element and the last element's right
                # neighbour will be the first element
                case "periodic":
                    for element in range(0, length):
                        newstate: int = rule_dict[
                          str(old_field[(element-1) % length])
                        + str(old_field[element])
                        + str(old_field[(element+1) % length])
                        ]
                        self.field[element] = newstate

                # Create a hard border by not changing the first and last
                # element. 
                case "constant":
                    for element in range(1, length-1): 
                        newstate: int = rule_dict[
                          str(old_field[(element-1)])
                        + str(old_field[element])
                        + str(old_field[(element+1)])
                        ]
                        self.field[element] = newstate
                
                case _:
                    print("NameError: " + str(boundary_condition) + 
                          " is not defined in the next_generation method, perhaps you made a typo" )
                    quit()

            # Stop the run when the spacebar or escape is pressed
            if ms.kbhit():
                if ord(ms.getch()) in [27, 32]:
                    quit()
        print("CA has done " + str(timesteps) + " timesteps")            
        field_history.append(self.field)
        super().display_CA(field_history)

    def __str__(self):
        '''Return a string of the field'''

        return str(self.field)


# Give the user some information on how to use the code and help the user
# when they give unusable inputs. 

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

    print("What should the length of the field be?")
    print("Please give your input as an integer between 3 and 1000.")

    length_input: str = input()
    control_for_int_type(length_input)
    length: int = int(length_input)
    control_length_value(length)

    print("")
    print("What border_condition and rule_number do you want to use? (seperated with a space)")
    print("For border_condition you can choose between 'periodic' and 'constant'.")
    print("For rule_number can choose an integer between 0 and 255.")


    rules = input().split(" ")

    border_condition: str = rules[0]

    rule_number_input:str = rules[1]
    control_for_int_type(rule_number_input)
    rule_number: int = int(rules[1])
    control_rule_number_value(rule_number)    

    print("")
    print("How many timesteps do you want to generate?")
    print("Please give your input as an integer between 0 and 1000.")

    timesteps_input: str = input()
    control_for_int_type(timesteps_input)
    timesteps: int = int(timesteps_input)
    control_timesteps_value(timesteps)

    
    one_dimension_CA(length, border_condition, rule_number, timesteps)


construct_CA_from_user_input()

