#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'caesarCipher' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. STRING s
#  2. INTEGER k
#


def caesarCipher(s, k):
    # Write your code here
    res = ""

    for char in s:
        if not char.isalpha():
            res += char
            continue

        code = k % 26

        base = ord("a") if char.islower() else ord("A")
        code += ord(char) - base

        if code > 25:
            code = code - 26

        res += chr(base + code)

    return res


caesarCipher("a", 28)
