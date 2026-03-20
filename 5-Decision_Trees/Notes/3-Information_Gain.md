# Information Gain and Decision Tree Splits

<img src="https://fox59.com/wp-content/uploads/sites/21/2023/03/KFC_Double_Down_PR_Hero.jpg" width="400px" />

## Overview

Recall that the basic decision tree algorithm considers splits based on each possible variable and chooses the split that gives the best separation between the two classes. In our previous note, we didn't have a way of quantifying the "best" split, but now we do: information entropy. This note discusses **information gain** as a strategy for picking splits when building a decision tree.

## Example: Sandwich or not?

Let's consider one of the trickiest philiosophical questions: what things are and are not sandwiches.
```
Food           Has Meat?    Has Bread?    Is Sandwich?
----           ---------    ----------    ------------
BLT               Yes          Yes            Yes
Sub               Yes          Yes            Yes
Pop-Tart           No           No             No
Burrito           Yes           No             No
PB & J             No          Yes            Yes
Hot dog           Yes          Yes             No
KFC double-down   Yes           No            Yes
```
