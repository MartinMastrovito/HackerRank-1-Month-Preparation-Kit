#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'plusMinus' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def plusMinus(arr):
    pos=0
    neg=0
    cero=0
    for i in arr:
        if i == 0:
            cero+=1
        else:
            if i > 0:
                pos+=1
            else:
                neg+=1
    print(pos / len(arr))
    print(neg / len(arr))
    print(cero / len(arr))

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
