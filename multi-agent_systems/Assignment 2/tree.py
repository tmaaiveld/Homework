from math import *
from random import random


class Tree:
    """Binary tree planted as a root and grown to any length"""
    def __init__(self):
        """Tree is formatted as a list of lists"""
        self.root = Node(None)
        self.tree = [[self.root]]

    def grow(self, depth):
        """Grows a tree of depth d"""
        for layer in range(depth):
            self.tree.append([])
            for node in self.tree[layer]:
                child1, child2 = node.expand()
                if layer == depth - 1:  # add a reward value to leaf nodes
                    child1.val, child2.val = int(random()*100), int(random()*100)
                self.tree[layer+1] = self.tree[layer+1] + [child1, child2]


class Node:
    """A split point on the tree"""
    def __init__(self, parent, value=None):
        self.v = int(random()*1000)
        self.l = None
        self.r = None
        self.parent = parent

    def expand(self):
        """Generate child nodes"""
        self.l = Node(self)
        self.r = Node(self)
        # self.v = 0
        return self.l, self.r

    def terminal(self):
        return self.l is None


class State:
    """A gamestate, i.e. an agent's position on the tree"""
    def __init__(self, node, parent=None):
        self.node = node
        self.l = None
        self.r = None
        self.parent = parent

        self.v_est = 0  # current value estimate
        self.t = 0
        self.n = 0      # number of times visited

    def expand(self):
        """Generate child states"""
        self.l = State(self.node.l, self)
        self.r = State(self.node.r, self)
        return self.l, self.r

    def leaf(self):
        return self.l is None
