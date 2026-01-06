# Node Counting

## Overview


## Problems


### Lights Out


<img src="https://miro.medium.com/v2/resize:fit:1185/1*Ee91-MD7MSjG5X9lvlOiqA.png" width="400px" />

*Example by K.L. deVries on [Medium](https://medium.com/swlh/programming-puzzle-lights-toggle-f4d27bf3683e)*


A classic puzzle. You're given a N x N grid of button lights, all of which are initially *ON*. Pressing a button toggles its state and the states of its four neighbors in the up, down, left and right directions. Your goal is to find the combination of button presses that turns all the lights *OFF*.

Implement a solution to the lights out puzzle using iterative deepening, then use your method to solve for progressively larger grids of *N* = 3, 4, 5, etc. **Create a graph** showing the number of nodes expanded to find the solution for each value of *N*. Work up to a value of *N* that requires 1-2 minutes of solution time (I don't know exactly what this will be).

Consider why iterative deepening is a good strategy for this problem. You're allowed to press each button as many times as you want, so there's no limit on the depth of any path. Left unchecked, you would simply descend the search tree, pressing buttons to create an infinitely long path that might never lead to a solution. Iterative deepening ensures that you consider all button combinations up to a certain depth before exploring deeper paths.

### Rubik's square
