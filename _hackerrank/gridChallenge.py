#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'gridChallenge' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING_ARRAY grid as parameter.
#


def gridChallenge(grid):
    # Write your code here
    for i, row in enumerate(grid):
        arr = list(row)
        arr.sort()
        grid[i] = "".join(arr)

    cols = []
    for c in range(len(grid[0])):
        res = []
        for r in range(len(grid)):
            res.append(grid[r][c])
        cols.append(res)

    for arr in cols:
        if arr != sorted(arr):
            print(f"failed: {arr}")
            return "NO"

    return "YES"


gridChallenge(["acb", "dfe", "cdf"])
