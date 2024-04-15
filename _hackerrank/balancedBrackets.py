#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'isBalanced' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#


def isBalanced(s):
    # Write your code here
    if len(s) % 2 != 0:
        return "NO"

    stack = []
    hmap = {"}": "{", "]": "[", ")": "("}

    for char in s:
        if char not in hmap:
            stack.append(char)
        else:
            if not stack or hmap[char] != stack.pop():
                return "NO"

    return "YES" if not stack else "NO"


print(isBalanced("}][}}(}][))]"))
