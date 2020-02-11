"""
WATCH THIS, VERY HELPFUL: https://www.youtube.com/watch?v=UXW2yZndl7U

Surprisingly difficult to create a nice data structure here! I probably went overboard with defining
the tree as a list of lists. Most likely there is no need for that, the objects all point to each other.
I might try restructuring it if I feel like it.

- Seems to be working pretty well, higher iteration count -> better scores
- tree is saved in referential object style, i.e. find a node via tree.l.l.r.r.l.l...
- but nodes are also saved in an array, this might be useful for analytics (indexing is complicated tho)
- might be good idea to reprogram some parameters to function arguments for testing
- rewards are random samples between 0 and 1000. The best score is (almost) always 999.

todo's
- Analyse results, plot reward, etc.
- Check system more thoroughly, but seems to work
- Might be interesting to map more info on the terminal states. Maybe find out how many of them
  are actually visited...
- using a seed or a set tree could help analyse results, or a deterministic max reward somewhere
  to see how often the algorithm successfully finds it
- parameter tuning on c is part of the assignment as well.

non-priority todo's
- lots of interesting stuff to think about with tree structures. For instance, trying to generate
  trees of depth 20 or more becomes increasingly difficult because of the exploding growth rate.
  However, a bit string implementation could be explored, where bit strings of length d point to
  some reward and the MC algorithm generates a search tree over these options... This depends on
  whether the tree of the problem itself actually NEEDS to be defined, in other words, if there
  are any essential properties to intermediary (non-terminal) states that the algorithm needs.
  I don't think that's the case, though.
- maybe only generate rewards for terminal nodes of game tree
- could work on how stuff is saved, the states and tree both are saved kinda oddly

- Don't think I did the tree implementation too well (I mean actual game tree, not MC tree).
  Only terminal nodes need rewards. Could instead build a 12-D numpy array where you can input
  twelve indexes to select a terminal node. Anyway, this is fine.
"""

from math import *
from random import random
from tree import Tree, State    # tree class could be simplified and might be redundant
import numpy as np
import matplotlib.pyplot as plt


def MCTS(state):
    """Run Monte Carlo Tree Search. states[-1] represents the current state."""
    states = [state]

    for i in range(max_it):
        if verbose:
            print('*** Iteration', i+1, '***')

        if not states[-1].leaf():  # if not on a leaf node:
            best_child = np.argmax([UCB(states[-1].l, c), UCB(states[-1].r, c)])
            states.append(states[-1].l) if best_child == 0 else states.append(states[-1].r)

        else:
            if states[-1].node.terminal():
                return  # end the sampling if terminal node is reached

            if not states[-1].n == 0:  # if state not visited before:
                    states[-1].expand()
                    states.append(states[-1].l)

            rollout_score = 0
            for k in range(max_rollouts):
                rollout_score += rollout(states[-1].node)

            for state in states:  # update values
                state.n += 1
                state.v_est += rollout_score/max_rollouts


def UCB(state, c=2):
    if state.n != 0:
        return state.v_est + c * sqrt(log(state.parent.n) / state.n)
    return inf


def rollout(node):
    """Performs a rollout from a leaf node"""
    while True:
        if verbose:
            print('rolling out...')

        if node.terminal():
            return node.v
        node = node.l if random() < 0.5 else node.r


def play(tree):
    state = State(tree.root)
    while True:
        MCTS(state)
        state = move(state)
        if state.node.terminal():
            return state.node


def move(state):
    best_move = np.argmax([state.l.v_est, state.r.v_est])
    return state.l if best_move == 0 else state.r


def terminal_states(tree):
    """Function that generates terminal state values and zips them with leaf nodes.
    Might be useful for analytics"""
    scores = []
    for leaf_node in tree.tree[-1]:
        scores.append(leaf_node)
    return zip(tree.tree[-1], scores)

# def best_score(tree):
#     """"""
#     best_score = 0
#     i=0
#     for leaf_node in tree.tree[-1]:
#         best_score = max(best_score, leaf_node.v)
#         i+=1
#     return best_score, tree.tree[i]  # return best node and score


### Program ###

# Parameters
d = 12
max_it = 10
max_rollouts = 1
c = 2
algorithm_runs = 100  # not the MCTS iterations, but repeats of the whole algorithm
verbose = False  # parameter sets whether functions print junk or not

# Initialize tree and run the algorithm n times
scores = []
for run in range(algorithm_runs):
    tree = Tree()
    tree.grow(d)
    final_state = play(tree)
    scores.append(final_state.v)

# Analytics
print(scores)
print(np.mean(scores))
plt.plot(scores)
plt.show()
## generate some plots
## generate some numbers
## do some parameter tuning on c
## do some more stuff