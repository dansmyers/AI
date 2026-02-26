# The Minimax Algorithm

##  An abstract game tree

<img src="Images/minimax_game_tree.png" width="500px" />

The previous note described the minimax concept: on my turn, I should choose the move that *maximizes* my score in the resulting game subtree, under the assumption that my opponent will play to *minimize* my score in each subtree.

The image above shows an **abstract game tree** illustrating the minimax concept. The upward and downward triangles represent move choices made by the maximizing and minimizing player, respectively. The leaves represent outcomes, with scores for each outcome. We don't have to care what the moves or scores represent in this tree, only that it alternates levels of minimizing and maximizing.

Consider the bottom-left subtree, with leaves of 5 and 6. The maximizing player seeks the greatest score, so he'll choose the move that yields 6. Likewise, in the next tree, he'll choose the move yielding 9, and so forth for every choice on the bottom level.

The minimizing player will always select the move that yields the minimum score through its subtree, under the assumption that the opponent is playing to maximize. The leftmost branch offer the minimizer a choice of a subtree with a best score of 6, or one with 9: the minimizer chooses the move that will lead to 6 as the best outcome. The rightmost tree offers choices that lead to outcomes of 10 and 5. The minimizer rationally chooses the 5 option.

At the root, the maximizer chooses the left branch, because it offers the highest score taking into account the minimizer's choices. Therefore, the best outcome the maximizer can obtain in this tree is 6.

## 
