# PinW-Cellulair-automata-project
Cellulair automata (CA) is a discrete model. CA consists of a regular grid of cells and each grid can be in one state of a finitive number of states. The simplest number of states is a boolean state (0 or 1). Example: 0 stands for dead cells and 1 for living cells.

The square CA have the following inputs:
- length of the CA
- the boundary condition

A bounday condition tells what we do with the cells on the border.

The one dimensional CA has also the following input:
- rule number

The rule number defines what the new state of a cell becomes with each state of the neigbours.

The two dimensional CA has also the following inputs:
- rule
- neighboorhood rule

The rule says what the new state must be for different number of neighbours.
The neighbourhood rule tells what cells around a cell are neighbours.

There is a abstract class the CA who have different chil classes. This is how the classes are constructed:
class CA:
  square CA:
    - one-dimensional CA
    - two-dimensional CA

Both the one-dimensional and two-dimensional CA are square CA who where each cell is a square.

