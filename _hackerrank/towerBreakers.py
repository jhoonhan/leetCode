#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'towerBreakers' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER m
#
def checkPossible(arr):
    for i in range(len(arr)):
        for j in range(1, arr[i]):
            x = arr[i]
            y = x - j
            if x % y == 0:
                arr[i] = y
                return arr
    return []


def towerBreakers(n, m):
    # Write your code here
    t_1 = [m] * n
    t_2 = [m] * n
    towers = [t_1, t_2]

    while True:
        for turn in range(2):
            print(f"turn: {turn +1}")

            towers[turn] = checkPossible(towers[turn])
            print(towers[turn])

            if not towers[turn]:
                if turn == 0:
                    print("player 2")
                    return 2
                else:
                    print("player 1")
                    return 1


towerBreakers(1, 7)
