#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'diagonalDifference' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY arr as parameter.
#


def diagonalDifference(arr):
    # Write your code here
    lr = 0
    rl = 0

    r1 = 0
    c1 = 0
    r2 = 0
    c2 = len(arr[0]) - 1
    while r1 < len(arr) and c1 < len(arr[0]) and r2 < len(arr) and c2 >= 0:
        cur1 = arr[r1][c1]
        cur2 = arr[r2][c2]
        lr += cur1
        rl += cur2

        r1 += 1
        c1 += 1
        r2 += 1
        c2 -= 1
    print(abs(lr - rl))
    return abs(lr - rl)


diagonalDifference([[1, 2, 3], [4, 5, 6], [9, 8, 9]])
