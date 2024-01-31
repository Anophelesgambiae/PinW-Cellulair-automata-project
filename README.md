# PinW-Cellulair-automata-project
Cellulair automata (CA) is a discrete model. CA consists of a regular grid of cells and each grid can 
be in one state of a finitive number of states. 
The simplest number of states is a boolean state (0 or 1). 
Example: 0 stands for dead cells and 1 for living cells.

With each tick the rule and cells on the field determines the next states of the cells. 
There plays recursion. We call this recursion the next generation method.
The rule of the CA determines how the recursion is going.

Because a computer cannot have a infinite grid of cells we must do something with the bordor. 
The constant boundary condition let all cells in the border constant, and the periodic
boundary condition 'paste' the border as a donut.

For the two-dimensionale-CA we have also the neighbour rule, this rule tells what cells around one cell are the neigbours.
This is used for the game of Life.

When running the program interesting patterns can be seen. 
For the game of life this patterns can be complex.


