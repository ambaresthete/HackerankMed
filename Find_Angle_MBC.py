# Enter your code here. Read input from STDIN. Print output to STDOUT
import math

AB = float(input())
BC = float(input())
cha = chr(176)
print(str(round(math.degrees(math.atan2(AB,BC))))+cha)
