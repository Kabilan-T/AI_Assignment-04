#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May 19 20:39:47 2018

@author: iswariya

Edited on Wed Dec 09 19:00:00 2020

@author: Kabilan Tamilmani
"""

import sys
import timeit
from heapq import *

from helper import *


def Astar_search(board, opt):
    """Function to implement the A-star search algorithm.

    Parameters
    ----------
    board : Puzzle
        object of class Puzzle which contains the puzzle configuration
    opt : int
        1 for Manhattan Dist heuristic, 2 for Misplaced Tiles heuristic

    Returns
    -------
    Sequence[int]
        path from unsolved puzzle to solved puzzle
    """

    priority_queue = []
    f_score = 0  # evaluation function value
    g_score = 0  # cost function value
    h_score = 0  # heuristic function value

    # Creating a heap from list to store the nodes with the priority h_score
    depth = 0
    heappush(priority_queue, (f_score, g_score, h_score, board.get_initial_state(),depth))

    # FILL IN YOUR CODE HERE
    node_relations =list([("", board.get_initial_state())])
    while len(priority_queue) > 0:
        _,_,_,current_node,depth = heappop(priority_queue) 
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
            g_score = depth
            for node in possible_moves:
                if opt ==1 : h_score = get_manhattan_distance(node)
                if opt ==2 : h_score = no_of_misplaced_tiles(node)
                f_score = g_score + h_score
                heappush(priority_queue, (f_score, g_score, h_score, node, depth+1))
                node_relations.append((current_node,node))
    return path


if __name__ == '__main__':

    puzzle1 = [0, 1, 2, 3, 4, 5, 8, 6, 7] # Initial Configuration for testing
    puzzle2 = [8, 7, 6, 5, 1, 4, 2, 0, 3] # Second Configuration for testing
    puzzle3 = [1, 5, 7, 3, 6, 2, 0, 4, 8] # Final Configuration for testing
    print("First configuration of puzzle")
    print_puzzle(puzzle1)
    print("Second configuration of puzzle")
    print_puzzle(puzzle2)
    print("Third configuration of puzzle")
    print_puzzle(puzzle3)

    puzzle_opt = int(input("Enter which configuration of puzzle to run (1 or 2 or 3 ) : "))
    if   puzzle_opt == 1 : puzzle_8 = puzzle1
    elif puzzle_opt == 2 : puzzle_8 = puzzle2
    elif puzzle_opt == 3 : puzzle_8 = puzzle3
    else : 
        print("Invalid Choice")
        sys. exit()
        
    print("\nSelected Configuration")
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
