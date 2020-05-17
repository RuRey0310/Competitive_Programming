import itertools
from collections import defaultdict
import collections
import math
import sys
sys.setrecursionlimit(200000)
mod = 1000000007

n = list(input())

if n[-1] == "3":
    print("bon")
elif n[-1] == "0" or n[-1] == "1" or n[-1] == "6" or n[-1] == "8":
    print("pon")
else:
    print("hon")