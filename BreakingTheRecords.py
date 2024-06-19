#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the breakingRecords function below.
def breakingRecords(scores):
    maxi=scores[0] #inicializamos la cantidad minima y maxima de todo
    mini=scores[0]
    maxcount =0
    mincount=0
    for i in range(len(scores)):#recorremos la 'lista' y guardamos el maximo, 
        if(scores[i]>maxi):     #cada vez que encontramos uno aumentamos la cantidas de maximos
            maxi = scores[i]    #lo mismo para los minimos
            maxcount+=1
        if(scores[i]<mini):
            mini = scores[i]
            mincount+=1
    return [maxcount, mincount] #retornamos las veces que se rompe el maximo y el minimo y lesto

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    scores = list(map(int, input().rstrip().split()))

    result = breakingRecords(scores)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()