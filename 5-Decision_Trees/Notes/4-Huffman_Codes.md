# Huffman Codes

## Overview

**Huffman coding** is a method of data encoding invented by David A. Huffman in 1952. The method takes a set of symbols and their probabilities of occurrence and constructs an encoding mapping each symbol to a binary string. These binary strings are *prefix-free*: no complete code is a prefix of any other code. The example we previously saw in the note on entropy is an example of a Huffman code.

You can view Huffman codes as a type of **lossless compression**. Given a binary code string and the mappings, the corresponding input symbols can be reconstructed unambiguously in time linear with the code string length.

If symbols have to be encoded individually, then Huffman codes are optimal, in the sense of minimizing the expected number of bits needed to transmit a message. This isn't always the optimal compression strategy: methods like run-length encoding drop the requirement to encode symbols individually and can compress multiple symbols at once.

## Method

The general Huffman strategy builds the coding from the bottom-up by constructing a binary tree. Each step of the process chooses two existing nodes to join together, creating a new subtree.

To start, create a new node for each symbol. Then repeatedly,

1. Choose the two nodes with the smallest probabilites
2. Create a new internal node with the two chosen nodes as its children
3. The probability of the new node is the combined weight of its children

This process continues until everything has been joined into a single tree. In pseudocode:
```
Huffman Coding

input:
    symbols - the list of symbols
    probs - the list of per-symbol probabilities

output:
    binary coding tree


// Initialize empty priority queue
heap = PriorityQueue()

// Insert starting symbols into queue
for i = 1 to length(symbols) {
    node = TreeNode()
    node.symbol = symbols[i]
    node.prob = probs[i]
    heap.insert(node)
}

// Main loop: repeatedly combine two lowest-weight nodes
while length(heap) > 1 {
    left = heap.min()
    right = heap.min()

    parent = TreeNode()
    parent.left = left
    parent.right = right
    parent.prob = left.prob + right.prob
}

// The one remainining node is the root of the entire tree
root = heap.min()
return root
```

### Practice question

Write a recursive method that will descend the tree and construct the code for each symbol. The function could be something like this:
```
build_codes(node, current_code) {

    // Base case: a leaf contains a symbol
    if node is a leaf {
        output its code and symbol
    }

    // Recursive case: process the left and right branches
    build_codes(node.left, ???)
    build_codes(node.right, ???)
}
```
Think about what to put in the `???` spaces. Tip: going left corresponds to adding a zero to the code string, going right corresponds to adding a 1.

## Example

Suppose we have the following symbols and probabilities.
```
Symbol | Probability
--------------------
  A    |     .05
  B    |     .15
  C    |     .25
  D    |     .35
  E    |     .20
```

The first step chooses the two smallest probabilities, A and B, and joins them together. Their combination has a probability of .20.
```

      .20
       |
    0  |  1
  -----------
 |           |
 A           B
```
It can be helpful to update the table:
```
Symbol | Probability
--------------------
  C    |     .25
  D    |     .35
  E    |     .20
 AB    |     .20
```
The next step combines E with the AB subtree for a combined weight of .40:
```
                    .40
                     |
              0      |    1
        --------------------------
       |                          |
    0  |  1                       |
  -----------                     |
 |           |                    |
 A           B                    E
```
The next step merges C and D into a subtree:
```
      .60
       |
    0  |  1
  -----------
 |           |
 C           D
```
And the final step merges the two subtrees together:
```
                                    1.0
                                     |
                             0       |       1
                      --------------------------------
                     |                                |
              0      |    1                       0   |  1
        --------------------------             ---------------
       |                          |           |               |
    0  |  1                       |           C               D
  -----------                     |
 |           |                    |
 A           B                    E
```
The final codes are:
```
A: 000
B: 001
C: 10
D: 11
E: 01
```
