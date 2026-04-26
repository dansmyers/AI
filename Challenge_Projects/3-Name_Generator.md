# Name Generation

<img src="https://upload.wikimedia.org/wikipedia/commons/thumb/b/b1/%22Flacking%22_d%27Ememem_%C3%A0_Lyon%2C_2021.jpg/960px-%22Flacking%22_d%27Ememem_%C3%A0_Lyon%2C_2021.jpg" width="300px" />

*Ememem is an artist based in France who repairs cracks in streets and sidewalks with tile mosaics. He calls the style "flacking" after flaque, the French word for puddle.

## Due 5/5 (last day of exams)

## Overview

This project will allow you to practice working with a neural network similar to a language model. The network we'll use will be trained on a list of names and learn to generate new names that are similar in structure to existing names.

We'll be working with [makemore](https://github.com/karpathy/makemore), a small neural network project made by Andrej Karpathy, a leading AI researcher. He's made a number of videos and other resources covering LLM design and implementation that are worth checking out.

The project has four phases:

- Analyze the existing list of names and create a statistical heatmap showing which letters are likely to follow each other

- Use your statistical model to generate some names and see how it performs on creating realistic but novel names

- Use the makemore model to generate some names

- Examine the statistical properties of the names produced by makemore and see how their letter sequences are similar to or different from the statistics found in the raw data


## Setup

Clone the makemore repository:
```
git clone https://github.com/karpathy/makemore
```
This will create a directory called `makemore` that has two files of interest: the Python script `makemore.py` and `names.txt`. The names file contains 32000 names, one per line.

You'll also need to install two libraries. The main one is Pytorch, which is used for neural network training.
```
pip install torch
pip install tensorboard
```

## Stats

Start by creating a script that processes the `names.txt` file.

The first step is to read each name, then append and prepend a '.' character to represent the start and end of the name. For example, `chelsea` would become `.chelsea.`. Real language models also do this, but with special token values that represent `<BEGINNING OF INPUT>` and `<END OF INPUT>`.

The second step is to build a **transition matrix** that records the number of times each letter follows each other letter. For example, if you had the name `.adelaide.` as your only example, the matrix would look like the following:

```
                     second letter

                  | .  a  d  e  i  l
                --------------------
               .  |    1  
               a  |       1     1
first letter   d  |          2
               e  | 1              1     
               i  |       1
               l  |    1
```
The matrix shows that 'i' is followed by 'd' in the one time it occurs. There are two times that 'e' comes after 'd', and so forth.

Once you have the matrix, you can visualize it as a heat map. Each row shows the distribution of subsequent characters for each starting character. The distribution shows what character combinations are likely in real names. Check out [this article](https://medium.com/@jayadevgh/i-followed-karpathys-bigram-model-makemore-here-s-what-i-learned-d9338f52cf47) for an example you can use as a model.

Answer the following questions:

- What are the three most likely and three least likely starting letters? Tip: Look at the row for '.', which shows the probabilities for every character that follows the starting '.'.
- Repeat for the ending letters, indicated by the '.' column. Are some letters more likely to end names than others?
- Are there are any letters following 'q' others than 'u'?
- What's the most likely second letter for names that start with 'x'?

## Generate

Now use your distribution to generate 25 new names. Here's the process in pseudocode:
```
letter = '.'
name = ''

while True:

    # Choose the next letter from the distribution of the current letter
    # You'll have to write the random_choice function
    letter = random_choice(distribution[letter])

    if letter == '.':
        break
    else:
        name += next_letter

print(name)
```
Add some checks to reject names with fewer than 3 non-dot letters.

Take a look at the names produced by your method. Do they seem realistic? What qualities do you observe?

## Train

Now run the makemore script. It trains a small transformer (basically the same as GPT-2) on the name set:
```
python makemore.py -i names.txt -o names
```
This will take a while. I suggest letting it run for ***at least*** 100,000 training steps before you stop the training process.

It will print some sampled names as it goes, but I recommend waiting until you've stopped training, then running the model in sample mode to generate new names. This mode uses the best saved model copy from training and runs it forward to produce outputs:
```
python makemore.py -i names.txt -o names --sample-only --seed 1
```
Change the seed parameter to get a different list of names. Record the new names that aren't in the training set until you have at least 200 names.

## Stats again

Repeat the heatmap creation process for the names produced by makemore. Compare that map to your first one from the real name data set. What similarities and differences do you observe?

## Submission

Turn in your two heatmaps, the list of generated names, and the written answers to the questions.


