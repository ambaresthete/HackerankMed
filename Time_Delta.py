#!/bin/python3
from datetime import datetime
import math
import os
import random
import re
import sys

# Complete the time_delta function below.
def time_delta(t1, t2):
    for _ in range(t):
        d1=datetime.strptime(''.join(t1),'%a %d %b %Y %H:%M:%S %z')
        d2=datetime.strptime(''.join(t2),'%a %d %b %Y %H:%M:%S %z')
        return str(int(abs((d1-d2).total_seconds())))

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        t1 = input()

        t2 = input()

        delta = time_delta(t1, t2)

        fptr.write(delta + '\n')

    fptr.close()
