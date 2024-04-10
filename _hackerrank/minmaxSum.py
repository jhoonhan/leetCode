import math
import os
import random
import re
import sys

#
# Complete the 'miniMaxSum' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#


def miniMaxSum(arr):
    # Write your code here
    arr.sort()
    res1 = sum(arr[0:4])
    res2 = sum(arr[len(arr) - 4 :])

    print(res1, res2)


miniMaxSum([1, 3, 5, 7, 9])
