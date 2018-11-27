#!/bin/python3

import math
import os
import random
import re
import sys
from collections import Counter, OrderedDict


if __name__ == '__main__':
    s = input()
    class OrderedCounter(Counter,OrderedDict):
        pass
    count = OrderedCounter(sorted(s))
    ans = count.most_common(3)
    for i,j in ans:
        print(i+" "+str(j))

