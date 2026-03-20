# Information Gain and Decision Tree Splits

<img src="https://fox59.com/wp-content/uploads/sites/21/2023/03/KFC_Double_Down_PR_Hero.jpg" width="400px" />

*The KFC Double-Down is a hypothesized, purely theoretical sandwich consisting of bacon and cheese between two fried chicken filets.*

## Overview

Recall that the basic decision tree algorithm considers splits based on each possible variable and chooses the split that gives the best separation between the two classes. In our previous note, we didn't have a way of quantifying the "best" split, but now we do: information entropy. This note discusses **information gain** as a strategy for picking splits when building a decision tree.

## Example: Sandwich or not?

Let's consider one of the trickiest philiosophical questions: what things are and are not sandwiches?
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


Note: I will not accept any arguments that the breading on the KFC chicken counts as "having bread"
```

In this dataset, `Is Sandwich?` is the decision variable of interest. Suppose that we're building a decision tree and need to choose the top-level split. We have two variables we could choose: `Has Meat?` or `Has Bread?`. We'd like to choose the variable that does the best job of splitting the two classes.

The basic strategy is to use entropy as our measure of split quality. You may be familiar with the general idea of entropy in physics as a measure of "disorder" in a system. Applied to a classification problem, a "high entropy" set corresponds to a collection of examples that are roughly balanced between the two classes. That is, a dataset with higher entropy is not strongly biased in favor of either class. A "low entropy" set would correspond to a collection dominated by one class or the other.

Therefore, we can compare the entropy of the total set to the entropies obtained by each candidate split and choose the split that gives us the best improvement in collective entropy, which corresponds to the split that does the best job of separating the two classes of interest. The *information gain* calculation formalizes this process.

### Step 1: calculate entropy of the complete data set

The top-level set has 4/7 sandwiches and 3/7 non-sandwiches. Therefore, its entropy is:

$$ -.5714 \log_2(.5714) - .4286 \log2(.4286) \approx .9852 $$

Don't worry about the exact entropy number! We can observe that it's close to 1, indicating that the classes are closer to equally split, but don't worry about interpreting the specific result.

### Step 2: Choose one split and calculate the entropies that result

Suppose we evaluate `Has Meat?` as the candidate. This separates the top-level set into two subsets:

- The `Yes` cases contain five examples, split into 3/5 sandwiches and 2/5 non-sandwiches
- The `No` cases contain two examples, one sandwich and one non-sandwich

The entropy for the `Yes` case is

$$ -.60 \log_2(.60) - .40 \log_2(.40) \approx .9709 $$

The entropy for the no case is

$$ -.50 \log_2(.50) - .50 \log_2(.50) = 1.0 $$

### Step 3: Take a weighted combination of the subset entropies

Splitting on `Has Meat?` gave us an unequal split, with 5 examples in the `Yes` case and 2 examples in the `No` case. This isn't necessarily bad: it might be fine to have an unequal split if it does a good job of pulling out a distinct subset that belongs to one class.

Calculate the weighted average entropy between the `Yes` and `No` cases. The `Yes` class contained 5 of the 7 total examples vs. 2 out of 7 for the `No` case, so the weighted average is:

$$ \frac{5}{7} \cdot .9709 + \frac{2}{7} \cdot 1.0 = .9792 $$

The information gain is the **reduction** in entropy compared to the original calculation:

$$ .9852 - .9792 = .0060 $$

Again, that number by itself doesn't tell us much. It's a quantification of how much splitting on `Has Meat?` improved the entropy of the decision tree. In this case, though, we might intuitively say that the split wasn't very good. In particular, the `No` case yielded no useful discrimination between the classes.

### Step 4: Repeat for other candidate splits

The method considers other options it might split on and evaluates the information gain of each one. Repeat the steps above for the `Has Bread?` variable and see what gain you obtain? Which variable is the better split?

Tip: You should get about .8571 for the weighted entropy of the split, for a gain of .1281.

## Gini impurity

An alternative to the information gain measurement is **Gini impurity**. It's defined as the probability that two randomly chosen items from the training set belong to different classes:

$$ G(X) = 1 - \sum_i p_i^2 $$

Equivalently, this is the probability that assigning an item a class chosen at random from the distribution of class labels results in a misclassification.

The name is a bit misleading. Carrado Gini was an Italian statistician who described a measurement of statistical inequality in 1912. That score is now called the Gini coefficient (or Gini index) and is often used in developmental economics when quantifying wealth inequality in a nation. The creators of the CART decision tree algorithm developed the impurity concept as part of their work in the 1980s and called it "Gini impurity", because it was somewhat inspired by Gini's original theory, even though the actual calculation is different.

Impurity doesn't reqwuire logarithms, so it's somewhat simpler to calculate the information gain, but the two measurements are similar in most practical cases. `scikit-learn` uses CART and Gini impurity as the defaults in its `DecisionTreeClassifier` implementation.


