#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'timeConversion' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#


def timeConversion(s):
    # Write your code here
    ampm = s[len(s) - 2 :]
    splitted = s[:-2].split(":")
    h = int(splitted[0])
    m = splitted[1]
    s = splitted[2]

    if ampm == "AM" and h == 12:
        h = 0

    if ampm == "PM" and h < 12:
        h += 12

    f_h = "{:02}".format(h)
    print(f"{f_h}:{m}:{s}")
    return f"{f_h}:{m}:{s}"


timeConversion("12:05:45AM")
