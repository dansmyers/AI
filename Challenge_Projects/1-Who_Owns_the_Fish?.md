# Who Owns the Fish?

<img src="https://upload.wikimedia.org/wikipedia/commons/thumb/9/96/Sander_vitreus.jpg/2560px-Sander_vitreus.jpg" width="40%" />

## Due Friday, 3/8 (the day before Spring Break)

## You can work with a partner to complete this problem

## Overview

This is my all-time favorite problem. It's often attributed to Einstein (there's no evidence he created it, of course), but has appeared in various forms since at least the 1960s.

> There are five houses in a row, each painted a different color. In each house lives a person with a different nationality. The five owners each drink a different drink, smoke a different brand of tobacco, and keep a different pet. One of the pets is a walleye pike.
> - The Brit lives in the red house
> - The Swede keeps dogs as pets
> - The Dane drinks tea
> - The green house is on the left of and next to the white house
> - The green house owner drinks coffee
> - The person who smokes Pall Malls keeps birds
> - The owner of the yellow house smokes Dunhills
> - The man living in the house right in the center drinks milk
> - The man who smokes Blends lives next to the one who keeps cats
> - The Norwegian lives in the first house
> - The man who keeps horses lives next to the one who smokes Dunhills
> - The owner who smokes Bluemasters drinks beer
> - The German smokes Princes
> - The Norwegian lives next to the blue house
> - The man who smokes Blends has a neighbor who drinks water
>
> Who owns the fish?

Your assignment is to write a program that uses backtracking search to solve the riddle. The book chapter posted on Canvas has a section that will lead you through an outline of the solution and give you tips on coding the constraints. Use it as your starting point.

- Start by solving the puzzle by hand, using the tips below if you want them
- You can write your solution in either Java or Python, your choice
- **Develop incrementally**: start by writing the basic solver that can produce a solution with no constraints, then add *one constraint at a time* until you get the final answer
- Use backtracking search; you don't need any other algorithm for this problem

## Solving the Puzzle

Begin with an image of the five houses in a line. Each house is like a basket of five attributes: *Nationality*, *Color*, *Drinks*, *Smokes*, and *Pet*. You can represent the solution in a table where each row is house and each attribute is a column. This will map to the matrix solution we'll use in the program.

Some information is given immediately in the puzzle.

```
House    Nationality    Color    Drinks    Smokes    Pet
-----    -----------    -----    ------    ------    ---
1         Norwegian
2                       Blue
3                                 Milk
4
5
```

***STOP READING HERE IF YOU DON'T WANT ANY MORE HINTS***


Here are some tips to help you get started:
- The first house can't be blue, red (the Brit lives in the red house), green (the green house must be next to the white house), or white (the white house can't be in the first position). Therefore, it must be yellow.

- The center house can't be green (the green house owner drinks coffee) or white. Therefore, it must be red.

- The owner of the yellow house smokes Dunhills and the Brit lives in the red house.

```
House   Nationality    Color    Drinks    Smokes    Pet
-----   -----------    -----    ------    ------    ---
1        Norwegian     Yellow
2                      Blue
3        Brit          Red       Milk
4
5
```

Keep going and work out the rest of the solution.
