# Sokobot

<img src="https://upload.wikimedia.org/wikipedia/commons/4/4b/Sokoban_ani.gif" width="300px" />

*Example Sokoban puzzle from Wikipedia*

## Overview

*Sokoban* ("warehouse keeper") is a puzzle game where the object is to push boxes onto storage locations. The original game was created by Hiroyuki Imabayashi in 1981 and published by the Thinking Rabbit company.

In this project, you're going to write an interactive Sokoban solver. The complete version will have a web-based interface where the user can load puzzles, submit them to be solved, and see the solution steps.

As in the other projects for this unit, the key is to *develop incrementally*. The solver itself will use A* search and you'll write that first. Once you have that working, you'll add more interface features.

## Details

You can play practice puzzles at [Sokoban Online](https://www.sokobanonline.com/play/tutorials/76067_classic-box) Try a few out.

The basic rules of the game are straightforward:

- The player controls the warehouse keeper who can move up, down, left, and right, one square at a time. Diagonal movement is not allowed.

- Boxes can only be pushed, not pulled

- Only one box can be pushed at a time. You can't use a box to push another box.

- The overall goal is to place each box on a storage location. Any box can be placed on any storage location - there are no assigned spots. A box can be moved onto a location and then moved off if necessary.

## Plan

Use these steps as a basic guideline for building the system. You can make any reasonable design decisions that you need to, but don't overcomplicate things until you have something working for each step.

Don't worry about optimizing to solve huge problems. It's okay if you stick to relatively small instances (approximately 8x8 squares or less, 5 boxes or less). You can crank things up once you're confident the system works.

### Discuss the problem

Start by chatting with Claude about solving Sokoban using A* search. In particular, think about strategies for the heuristic and rules for detecting when boxes are stuck, which will allow you to prune bad states.

You'll also want to think about the puzzle representation: do you want to use a matrix that stores the map, or some more compact representation with the coordinates of the player, boxes, locations, and walls? Many options are possible, just make sure you are making a conscious choice about what you want to use.

A simple strategy is to compute the Manhattan distance from each box to its nearest storage space. That's a lower bound on the real solution distance, but there are some other heuristics that will be better. Consider precomputing distances from each square on the map to each goal to speed up the heuristic evaluation.

- **Tip**: Chat about the [Hungarian algorithm](https://en.wikipedia.org/wiki/Hungarian_algorithm) as a heuristic. It will allow you to match each box to a storage location such that the overall cost of all the matches is minimized. This is still a lower bound on the real solution distance because it ignores the need to make extra moves to avoid blocking situations as you move the boxes around.

Claude may suggest ideas like precomputing subproblem solutions. I don't think you need to do this; you can try it as an extension later if you want.

By the end of this phase, you should have an understanding of how the solver is going to work at an algorithmic level. Ask Claude to output a `solver.md` file summarizing the design.

### Build the solver

This is going to be the key part. I'm going to say it again: **develop step-by-step and test as you go**.

Chat with Claude Code about a phased implementation plan with tests for each step. Make sure that you understand what's being tested and that the tests pass before you move on to the next phase. Other than that, I don't have a lot of concrete suggestions for this process: it's mostly going to be implementing the plan you developed in the first stage, while avoiding the temptation to let things rip and generate so much code that you can't understand it.

At the final step, make sure that you can solve simple puzzles end-to-end and output the solution steps to verify that they're correct.

### Web interface

Once you have the solver working, add a web interface, where the user can load puzzles on a front-end page, then send them to the back-end solver to be processed. Once the puzzle is solved, display the solution step-by-step for the user to verify. Your server only needs to process one puzzle at a time.

Use Python Flask for the back-end and create an API function that the front-end can call to submit a puzzle to be solved. You'll have to decide on the submission format and the representation of the returned solution.

For this version, I recommend having a simple choice to load one of a small number of pre-designed puzzles.

**Make sure the solver works** before you try this part. Think about our key idea of *encapsulation*. If the solver is its own self-contained component, then you can focus on the front-end/back-end interactions without having to touch the solver code.

Use the standard strategy of designing a specs document for the interface, then building it step-by-step.

### Puzzle designer

For the final step, add the ability for the user to design puzzles and then solve them. Give the user some controls (you can decide on the interface) to set the size of the room and place the boxes, storage locations, and walls.

Again, think carefully about how you're going to store the puzzle the user is building and then convert that into the form that will be sent to the solver.

## Good luck!

I admit that I'm pushing hard here to see what we can do with these new tools. If this turns out to be too tricky, then that will be a valuable lesson and we'll adjust. If it turns out to be too *easy*, well...
