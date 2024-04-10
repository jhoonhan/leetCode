#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'countingSort' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY arr as parameter.
#


def countingSort(arr):
    # Write your code here
    result = [0] * 100

    for i in arr:
        result[i] += 1

    print(result)
    return result


countingSort([0, 1, 3, 2, 1, 4])
