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


def towerBreakers(n, m):
    winner = 0

    if m == 1:
        winner = 2
    elif n % 2 == 0:
        winner = 2
    else:
        winner = 1

    return winner


towerBreakers(1, 7)
