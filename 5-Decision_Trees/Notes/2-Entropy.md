# Entropy and Information Theory

## Overview

Claude Shannon is one of the most important engineers of the 20th Century and a central figure in the history of computing. In 1937, as a graduate student and MIT, he authored a Master's thesis titled *A Symbolic Analysis of Relay and Switching Circuits*, which showed that concepts of Boolean algebra could be used to create digital logic circuits and laid the foundation for the design of all subsequent electronic computers.

In 1948, he published *A Mathematical Theory of Communication* as a report in the *Bell System Technical Journal*, establishing **information theory** as a mathematical framework for understanding telecommunications and signal processing. The concepts of information theory have important applications in computer security, cryptography, and in data compression. For us, Shannon's idea of **information entropy** will be our main tool for choosing splits in a decision tree.

## Information and uncertainty

Information theory is concerned with encoding the *information content* of a signal.

Suppose you have two researchers, A and B, who are performing a coin flipping experiment. A will repeatedly flip the coin, then transmit the sequence of outcomes to B. Each coin flip has two outcomes with equal probability, so the result of a single flip can be encoded using one bit. Therefore, A can encode the result of *N* flips as a sequence of *N* bits and send it to B. We can say that the outcome of a single coin flip represents *one bit* of information and that sequence of *N* flips represents *N* bits of information.

From B's perspective, receiving a sequence of bits from A corresponds to *resolving uncertainty*. Before receiving the communication, B didn't know the outcome of any flips, and after receiving *N* bits he knows *N*.

Also observe that we can't really do better than using 1 bit per flip in order to encode the information of this stream. The coin flips are independent and uncorrelated, so there is no general strategy to send the result of *N* flips that's more efficient that simply encoding them as *N* bits.

Consider, however, a 1 GB file that contains only zero-valued bytes. The file is large, but its *information content* is low. We could practically compress the file using an encoding to represent "0 repeated 1G times*. That encoding is sufficient to remove all uncertainty about the file's exact content.

## Probabilistic signals

Information theory is fundamentally statistical. We consider the signal of interest to be drawn from a collection of *symbols*, each of which has an associated probability of being selected. In the coin flipping example, the two symbols are "heads" and "tails", each with probability .50.

Here's another example. Suppose we have four symbols: A, B, C, and D.

- A occurs with probability .50
- B occurs with probability .25
- C occurs with probability 3/16 = .1875
- D occurs with probability 1/16 = .0625

We need a scheme for encoding an arbitrary sequence of A, B, C and D values as bits. How could we do this efficiently? One option is to use two bits for each symbol: for example, let A be 00, B be 01, and so forth. In that case, any sequence of *N* symbols requires 2*N* bits.

Intuitively, though, using the same length for every symbol is not maximally efficient. We should try to encode the most common symbols in the *smallest number of bits*. Suppose we did the following:
```
        |
    0   |   1
 ---------------
|               |
A            0  |  1
          -------------
         |             |
         B          0  |  1 
                 -------------
                |             |
                C             D
```
Let A be encoded as a single `0`, B as `10`, C as `110`, and D as `111`. Taking into account the probabilities of occurrence, the average bits per symbol is now

$$ 1 \cdot .50 + 2 \cdot .25 + 3(.1875 + .0625) = 1.75 $$

Therefore, in this example, a sequence of *N* symbols is expected to convey 1.75*N* bits of information. 

This type of efficient encoding is called a **Huffman code**. It's the theoretically optimal representation if we're constrained to encode each symbol as as fixed whole number of bits.

## Entropy calculation

Shannon's entropy is the formal theoretical version of the above example.


### Self-information

Consider symbol *i* that occurs with probability *p*<sub>*i*</sub>. The *self-information* of symbol *i* depends on its probability of occurrence and is given by:

$$ I(p_i) = -\log_2(p_i) $$

If *p*<sub>*i*</sub> = .50, then *i* has 1 bit of self-information. Smaller values of *p*<sub>*i*</sub> correspond to more bits of information. Intuitively, the lower the probability of a symbol, the more information is gained by observing its appearance.

I find it helpful to think of this as the *theoretical minimum* number of bits that should be used to encode symbol *i*, if we were allowed to use fractional bits. For example, if *p*<sub>*i*</sub> = 3/16, the theoretical number of bits for that symbol is

$$ -\log_2(.1875) \approx 2.415 $$

This is a little better than the previous example, where we were constrained to use whole bits for the encoding.

### Entropy of multiple symbols

The entropy of a collection of symbols is the expected value of their self-information values. Let *X* be a discrete random variable. The entropy of *X* is given by:

$$ H(X) = - \sum_i p_i \log_2(p_i) $$

Consider a few cases:

- If *X* is a single coin flip, it has 1 bit of entropy
- If *X* only takes on a single value with probability 1, then it has 0 bits of entropy
- Lower entropies correspond to random variables that are more predictable
- Higher entropies correspond to variables with more equally-distributed (that is, less predictable) outcomes

For our previous example, the exact entropy calculation is:

$$ -.50 \log_2(.50) - .25 \log_2(.25) - .1875\log_2(.1875) - .0625\log_2(.0625) \approx 1.7028 $$

Notice that this is a little better than the exact encoding, because the exact entropy calculation isn't constrained to use a whole number of bits for each symbol.

### Practice questions

Calculate the entropies of:

- A weighted coin that comes up heads 99% of the time
- A standard six-sided die
- A random variable representing the number of heads obtained by flipping three coins
