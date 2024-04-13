#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'superDigit' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. STRING n
#  2. INTEGER k
#


def superDigit(n, k):
    # Write your code here
    sub_sum = 0
    for num in n:
        sub_sum += int(num)
    s = str(sub_sum * k)

    def recur(s):
        res = 0
        if len(s) == 1:
            return s

        for c in s:
            res += int(c)

        res = recur(str(res))

        return res

    res = recur(s)

    return res


superDigit("9875", 4)
