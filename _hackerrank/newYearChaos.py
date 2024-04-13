#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'minimumBribes' function below.
#
# The function accepts INTEGER_ARRAY q as parameter.
#


def minimumBribes(q):
    # Write your code here
    bribe = 0
    for i in range(len(q) - 1, 0, -1):
        if q[i] != i + 1:
            if q[i - 1] == i + 1:
                bribe += 1
                q[i - 1], q[i] = q[i], q[i - 1]
            elif q[i - 2] == i + 1:
                bribe += 2
                q[i - 2], q[i - 1], q[i] = q[i - 1], q[i], q[i - 2]
            else:
                print("Too chaotic")
                return

    print(bribe)


minimumBribes([2, 1, 5, 3, 4])
