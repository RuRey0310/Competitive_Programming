import math
a, b, c = map(int, input().split())

if (pow(a,0.5)+pow(b,0.5)) < pow(c,0.5):
    print("Yes")
else:
    print("No")