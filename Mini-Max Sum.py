#!/bin/python3

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
    #ordenamos los numeros
    sorted_numeros = sorted(arr)

    #sumamos los 4 mas pequenos

    min=sum(sorted_numeros[:4])

    #sumamos los 4 mas grandes

    max = sum(sorted_numeros[1:])

    print(min ,max)

if __name__ == '__main__':

    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr) 