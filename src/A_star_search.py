#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May 19 20:39:47 2018

@author: iswariya
"""

import sys
import timeit
from heapq import *

from helper import *


def Astar_search(board, opt):
    """Function to implement the A-star search algorithm.
    Please use the functions in helper.py to complete the algorithm.
    Please do not clutter the code this file by adding extra functions.
    Additional functions if required should be added in helper.py

    Parameters
    ----------
    board : [type]
        [description]
    opt : [type]
        [description]

    Returns
    -------
    [type]
        [description]
    """

    priority_queue = []
    f_score = 0  # evaluation function value
    g_score = 0  # cost function value
    h_score = 0  # heuristic function value

    # Creating a heap from list to store the nodes with the priority h_score
    heappush(priority_queue, (f_score, g_score, h_score, board.get_initial_state()))

    # FILL IN YOUR CODE HERE
    node_relations =list()
    while len(priority_queue) > 0:
        g_score,_,_,current_node = heappop(priority_queue) 
        if board.goal_test(current_node):
            path = [current_node]
            while current_node != board.initial_state:
                for  node_relation in node_relations:
                    if current_node == node_relation[1]:
                        current_node = node_relation[0]
                        path.append(current_node)
                        break
            path = path[::-1]
            for i in path: print_puzzle(i)
            print("No. of moves made: ",len(path))
            break
        else:
            possible_moves = get_possible_moves(current_node,board)
            for node in possible_moves:
                if opt ==1 : h_score = get_manhattan_distance(node)
                if opt ==2 : h_score = no_of_misplaced_tiles(node)
                f_score = g_score + h_score
                heappush(priority_queue, (f_score, g_score, h_score, node))
                node_relations.append([current_node,node])
    return path


if __name__ == '__main__':       
    puzzle_8 = [0, 1, 2, 3, 4, 5, 8, 6, 7] # Initial Configuration for testing
    # puzzle_8 = [8, 7, 6, 5, 1, 4, 2, 0, 3] # Second Configuration for testing
    # puzzle_8 = [1, 5, 7, 3, 6, 2, 0, 4, 8] # Final Configuration for testing

    print("Initial Configuration")
    board = Puzzle(puzzle_8)
    print_puzzle(puzzle_8)
    opt = int(sys.argv[1])

    if opt == 1 or opt == 2:

        if opt ==1:
            print("\nRunning A star search with Manhattan Dist heuristic\n")
        else:
            print("\nRunning A star search with Misplaced Tiles heuristic\n")

        start_time = timeit.default_timer()
        Astar_search(board, opt)
        end_time = timeit.default_timer()
        print('Time: {}s'.format(end_time-start_time))
    else:
        print("Invalid Choice")
