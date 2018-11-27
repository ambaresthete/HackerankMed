# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import Counter, OrderedDict

n = int(input())
words = []
for k in range(0,n):
    s = str(input())
    words.append(s)
class OrderedCounter(Counter, OrderedDict):
    pass
count = OrderedCounter(words)
ans = len(count)
print(ans)
for i,j in count.items():
    print(j,end=" ")

