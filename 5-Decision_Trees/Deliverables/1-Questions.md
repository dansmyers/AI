# Decision Tree Questions

<img src="https://imgs.xkcd.com/comics/map_age_guide_2x.png" width="100%" />


## Predictable Fun

Consider the example data set below for toys my children own:

```
    Color    Size    Type       Is Fun?
    -----    ----    ----       -------
    red      big     truck      yes
    blue     small   dinosaur   no
    red      big     truck      yes
    red      small   dinosaur   no
    blue     small   truck      yes
```

- Calculate the entropy for the entire data set, using Is Fun? as the class label.

- For each of the three features (color, size, and type) determine the information gain that results from splitting the overall data set into two subsets using the feature.

- Which feature split gives the greatest information gain?


## Code

Construct the Huffman codes for the following set of symbols:
```
Symbol | Probability
--------------------
  A    |   .14
  B    |   .06
  C    |   .22
  D    |   .23
  E    |   .09
  F    |   .11
  G    |   .15 
```

What is the expected average number of bits used per symbol for your encoding, taking into account the probabilities of occurrence?
