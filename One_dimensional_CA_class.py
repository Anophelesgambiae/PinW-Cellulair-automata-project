import numpy as np
import time
import copy
import msvcrt as ms
import matplotlib as plot

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

    def __init__(self, length, boundary_condition,
                 rule_number, starting_field, timesteps) -> None:
        '''Return the starting field and the dictionary of the CA''' 

        # Create the dictionary for the rule. The input represents the
        # element's neighbour, the element itself and the element's right
        # neighbour
        rule_dict = {"111":0, "110":0, "101":0, "100":0, 
                     "011":0, "010":0, "001":0, "000":0}
        binary_number = "{0:08b}".format(rule_number)
        binary_list = list(binary_number)
        key_items_list = ["111", "110", "101", "100",
                          "011", "010", "001", "000"]
        i = 0
        for key in key_items_list:
            rule_dict[key] = int(binary_list[i])
            i += 1
        self.rule_dict = rule_dict

        if starting_field == "random":
            
            # Initialize the field where the elements have a 50% chance to be
            # a zero and 50% chance to be a one
            self.field = np.zeros(length, dtype = int)
            for item in range(0, len(self.field)):
                self.field[item] = np.random.choice(np.arange(0, 2),
                                                    p=[0.5, 0.5])
        
        self.Next_generation(length, boundary_condition, rule_dict, timesteps)

    def Next_generation(self, length, boundary_condition,
                        rule_dict, timesteps):
        ''' Return the next generation of the CA '''

        field_history = []
        for t in range(0, timesteps):
            old_field = copy.deepcopy(self.field)
            field_history.append(old_field)
            match boundary_condition:

                # Create a periodic border by adding %length when looking at
                # the neighbours so that the first element's left neighbour
                # will be the last element and the last element's right
                # neighbour will be the first element
                case "periodic":
                    for element in range(0, length):
                        newstate = rule_dict[
                          str(old_field[(element-1) % length])
                        + str(old_field[element])
                        + str(old_field[(element+1) % length])
                        ]
                        self.field[element] = newstate

                # Create a hard border by not changing the first and last
                # element. 
                case "constant":
                    for element in range(1, length-1): 
                        newstate = rule_dict[
                          str(old_field[(element-1)])
                        + str(old_field[element])
                        + str(old_field[(element+1)])
                        ]
                        self.field[element] = newstate
        
            # Stop the run when the spacebar or escape is pressed
            if ms.kbhit():
                if ord(ms.getch()) in [27, 32]:
                    quit()
        field_history.append(self.field)
        super().display_CA(field_history)

    def __str__(self):
        '''Return a string of the field'''

        return str(self.field)


# Give the user some information on how to use the code and help the user
# when they give unusable inputs 
print("What should the length of the field be?")
print("Please give your input as an integer greater than or equal to 3.")
length = int(input())
if length < 3:
    print("ValueError: Please choose a value greater than or equal to 3.")
    quit()
print("What border condition do you want to use?")
print("You can choose between 'periodic' and 'constant'.")
border_condition = input()
if border_condition not in ["periodic", "constant"]:
    print("NameError: perhaps you made a typo?")
    quit()
print("What rule number do you want to use?")
print("You can choose an integer between 0 and 255.")
rule_number = int(input())
if rule_number > 255 or rule_number < 0:
    print("ValueError: please give an integer between 0 and 255.")
    quit()
print("What starting field do you want to use?")
print("You can give a self chosen field in the form of an array or you can")
print("let a random field generate.")
print("For example '[0 1 0 0 0 1 1]' or 'random'.")
starting_field = input()

# Checks if the user tried to give a list or if the user tried to type random
if "]" and "[" in starting_field:

    if starting_field != length:
        print("ValueError: please make sure the given length and the length")
        print("of the given field are te same.")
        quit()
elif starting_field != "random":
    print("NameError: perhaps you made a typo.")
    quit()
print("How many timesteps do you want to generate?")
print("Please give your input as a postive integer.")
timesteps = int(input())
if timesteps < 1:
    print("ValueError: please give a positive value.")
    quit()

# The plotted CA for the user given inputs
plotted_CA = one_dimension_CA(length, border_condition, rule_number,
                              starting_field, timesteps)
