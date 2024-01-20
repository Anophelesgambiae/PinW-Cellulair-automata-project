import numpy as np
import time
import copy
import msvcrt as ms

from Square_CA_class import square_CA


class one_dimension_CA(square_CA):
    '''
    Here a class for one dimensional CA's is created.

    The inputs are as follows:
    -length: An integer of the length of the field
    -boundary-condition: "constant" for a system with borders
     and "periodic" for a borderless field
    -rule_number: The rule number used for the CA
    '''

    def __init__(self, length, boundary_condition, rule_number) -> None:
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

        # Initialize the field where the elements have a 50% chance to be a
        # zero and 50% chance to be a one
        self.field = np.zeros(length, dtype = int)
        for item in range(0, len(self.field)):
            self.field[item] = np.random.choice(np.arange(0, 2), p=[0.5, 0.5])

        print(self.field)
        self.Next_generation(length, boundary_condition, rule_dict)

    def Next_generation(self, length, boundary_condition, rule_dict):
        ''' Return the next generation of the CA '''

        while True:
            time.sleep(1)            
            old_field = copy.deepcopy(self.field)
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
                # element
                case "constant":
                    for element in range(1, length-1): 
                        newstate = rule_dict[
                          str(old_field[(element-1)])
                        + str(old_field[element])
                        + str(old_field[(element+1)])
                        ]
                        self.field[element] = newstate

            print(self.field)

            # Stop the run when the spacebar is pressed
            if ms.kbhit():
                if ord(ms.getch()) == 32:
                    break

    def __str__(self):
        '''Return a string of the field'''

        return str(self.field)

Printed_CA = one_dimension_CA(int(input()), input(), int(input()))
'''Return the CA for the given input'''
