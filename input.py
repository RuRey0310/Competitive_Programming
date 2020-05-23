#デフォルト
import itertools
from collections import defaultdict
import collections
import math
import sys
sys.setrecursionlimit(200000)
mod = 1000000007

n = int(input())
a, b = map(int, input().split())
a = list(map(int,input().split()))
a = [int(input()) for i in range(n)]
ab = [list(map(int, input().split())) for i in range(n)]

# graph作成
graph = {i: [] for i in range(1, n + 1)}
for _ in range(m):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)
    
#標準入力
a = int(input())

#1 2 3 4 5...n(数字)
b = list(map(int,input().split()))

#abcde...(文字列分割して配列に入れる)
c = list(input())

#n回複数行とる
n=0
string_list = [input() for i in range(n)]
int_list = [int(input()) for i in range(n)]

#2次元配列n回
k = [list(map(int, list(input().split()))) for i in range(n)]

#a[1] b[1]
#a[n] b[n]
a, b= [0] * n, [0] * n
for i in range(n):
    a[i], b[i] = map(int, input().split())

#配列を任意の値・要素数で初期化
l = [0] * 10
#二次元配列初期化
dp = [[0] * (n + 1) for i in range(3)]

#絶対値
abs(x=1)