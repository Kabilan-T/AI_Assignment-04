#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May 19 20:28:19 2018

@author: iswariya
"""

import copy
import math
from heapq import *

PUZZLE_TYPE = 8
ROW_SIZE = int(math.sqrt(PUZZLE_TYPE + 1))


class Puzzle:
    """ Class for creating N puzzle game environment.
    This class has been implemented to provide a minimalistic
    game environment to you. Please try to avoid modifying this
    class unless absolutely necessary.
    """

    def __init__(self, init_state):
        """Class Construction for initializing the board

        Parameters
        ----------
        init_state : list
            Initial position of the board obtained from user
        """

        self.initial_state = init_state
        self.goal_state = [i for i in range(0, PUZZLE_TYPE + 1)]
        self.explored_states = []

    def get_goal_state(self):
        """Class method to get the goal state of the board

        Returns
        -------
        list
            Configuration of board when goal state has been reached
        """

        return self.goal_state

    def get_initial_state(self):
        """Class method to get the initial state of the board

        Returns
        -------
        list
            Initial configuration of board during start of search
        """

        return self.initial_state

    def goal_test(self, node):
        """Class method to test if goal state is reached and 
        appends the particular board configuration to the list
        of explored states. Returns true if goal state is reached.

        Parameters
        ----------
        node : list
            Board configuration obtained from the search tree

        Returns
        -------
        boolean
            Returns true if the passed configuration is equal to
            goal configuration
        """

        self.explored_states.append(node)
        return node == self.goal_state

    def is_explored(self, node):
        """Class method to check if a particular board configuration
        has already been explored

        Parameters
        ----------
        node : list
            Board configuration obtained from the search tree

        Returns
        -------
        boolean
            Returns true if a particular configuration has already been explored
        """

        return node in self.explored_states


def print_puzzle(puzzle):
    """Function to print the puzzle to console

    Parameters
    ----------
    puzzle : list
        8 puzzle configuration
    """

    for idx, val in enumerate(puzzle):

        if (idx + 1) % ROW_SIZE == 0:     
            print("  ", val)
        else:
            print("  ", val, end="")
    print("-"*15)

    return


def move_left(position):
    """Function to move one position left in 8 puzzle if possible

    Parameters
    ----------
    position : list
        current configuration of the puzzle

    Returns
    -------
    list
        puzzle configuration after moving '0' to left
    """

    moved_position = position[:]
    idx = position.index(0)
    moved_position[idx],moved_position[idx-1]=position[idx-1],position[idx]
    return moved_position


def move_right(position):
    """Function to move one position right in 8 puzzle if possible

    Parameters
    ----------
    position : list
        current configuration of the puzzle

    Returns
    -------
    list
        puzzle configuration after moving '0' to right
    """

    moved_position = position[:]
    idx = position.index(0)
    moved_position[idx]=position[idx+1]
    moved_position[idx+1]=position[idx]
    return moved_position


def move_up(position):
    """Function to move one position up in 8 puzzle if possible

    Parameters
    ----------
    position : list
        current configuration of the puzzle

    Returns
    -------
    list
        puzzle configuration after moving '0' to up
    """

    moved_position = position[:]
    idx = position.index(0)
    moved_position[idx],moved_position[idx-ROW_SIZE]=position[idx-ROW_SIZE],position[idx]
    return moved_position


def move_down(position):
    """Function to move one position down in 8 puzzle if possible

    Parameters
    ----------
    position : list
        current configuration of the puzzle

    Returns
    -------
    list
        puzzle configuration after moving '0' to down
    """

    moved_position = position[:]
    idx = position.index(0)
    moved_position[idx],moved_position[idx+ROW_SIZE]=position[idx+ROW_SIZE],position[idx]
    return moved_position


def get_possible_moves(node, board):
    """Function to check whether a move is possible in left,
    right, up, down direction and store it.

    Parameters
    ----------
    node : list
        current configuration of the puzzle
    board : Puzzle (user defined class)
        currrent puzzle object

    Return
    ------
    list
        list of possible movements from current node
    """

    possible_moves = []
    # HINT :
    # 1. Convert the list to a heap and push the possible moves
    # to the heap based on priority.
    # 2. Please note priority depends on your search algorithm
    # For Eg: A-star uses f_score as priority while greedy search
    # uses h_score as priority

    board.explored_states.append(node)
    moves = []
    idx = node.index(0)
    if idx%ROW_SIZE >0:     moves.append(move_left(node))
    if idx%ROW_SIZE <2:     moves.append(move_right(node))
    if idx//ROW_SIZE >0:    moves.append(move_up(node))
    if idx//ROW_SIZE <2:    moves.append(move_down(node))
    possible_moves = [move for move in moves if not board.is_explored(move)]
    return possible_moves


def no_of_misplaced_tiles(node):
    """Function to get the number of misplaced tiles for a
    particular configuration

    Parameters
    ----------
    node : list
        current configuration of the puzzle

    Return
    ------
    int
        number of misplaced tiles
    """
    misplaced_tiles_count = 0
    for i in range(0, PUZZLE_TYPE + 1):
        if node[i]!=i:
            misplaced_tiles_count+=1
    return misplaced_tiles_count


def misplaced_tile_heuristic(nodes, possible_moves):
    """Function to implement misplaced tiles heuristic in
    combination with no_of_misplaced_tiles() for each of
    the search algorithms

    Parameters
    ----------
    node : [type]
        [description]

    Return
    ------
    [type]
        [description]
    """

    raise NotImplementedError


def get_manhattan_distance(node):
    """Function to calculate the manhattan distance for a
    particular configuration

    Parameters
    ----------
    node : list
        current configuration of the puzzle

    Return
    ------
    int
        manhattan distance for current configuration
    """
    manhattan_distance = 0
    for i in range(0, PUZZLE_TYPE + 1):
        if node[i]!=i:
            idx_1, idx_2 = i, node[i]
            x1, y1 = idx_1//ROW_SIZE, idx_1%ROW_SIZE,
            x2, y2 = idx_2//ROW_SIZE, idx_2%ROW_SIZE
            manhattan_distance += abs((x2-x1))+abs((y2-y1))
    return manhattan_distance


def manhattan_distance_heuristic(nodes, possible_moves):
    """Function to implement manhattan distance heuristic in
    combination with get_manhattan_distance() for each of
    the search algorithms

    Parameters
    ----------
    node : [type]
        [description]

    Return
    ------
    [type]
        [description]
    """

    raise NotImplementedError
