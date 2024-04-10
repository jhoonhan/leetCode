#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'lonelyinteger' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY a as parameter.
#


def lonelyinteger(a):
    # Write your code here
    hset = set()
    for num in a:
        if num not in hset:
            hset.add(num)
        else:
            hset.remove(num)
    print(list(hset)[0])
    return list(hset)[0]


lonelyinteger([1, 2, 3, 4, 3, 2, 1])
