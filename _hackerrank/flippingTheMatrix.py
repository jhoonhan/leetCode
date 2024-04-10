#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'flippingMatrix' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY matrix as parameter.
#


def flippingMatrix(matrix):
    # Write your code here
    n = len(matrix)
    res = 0
    for r in range(n // 2):
        for c in range(n // 2):
            res += max(
                matrix[r][c],
                matrix[r][n - c - 1],
                matrix[n - r - 1][c],
                matrix[n - r - 1][n - c - 1],
            )
    return res


flippingMatrix(
    [
        [101, 201, 83, 201, 100],
        [301, 400, 56, 400, 301],
        [15, 78, 101, 43, 28],
        [301, 400, 114, 400, 301],
        [100, 201, 62, 201, 100],
    ]
)
