#最大公約数
#最小公倍数
import math
math.gcd()
math.lcm()

#sort 昇順、降順 二次元配列
a=[]
a.sort(key = lambda x: x[1])
a.sort(key = lambda x: x[1] , reverse = True)

#正の無限大,負の無限大
x = float("inf")
y = float("-inf")

#bit全列挙
n = 2
for i in range(2 ** n):
    switch = [0] * n
    for j in range(n):
        if((i >> j) & 1):
            switch[j] = 1

#絶対値
abs(n)

#アスキーコード
ord("a")

#素数
def Prime(n):
    for p in range(2, n):
        if n % p == 0:
            return False
    return True

#エラトステネスのふるい
MAX = 100010
is_prime = [True] * MAX
is_prime[0] = False
is_prime[1] = False
for i in range(2, MAX):
    if is_prime[i]:
        j = i * 2
        while j < MAX:
            is_prime[j] = False
            j += i

#辞書型
d = {"a": 1, "b": 2}

#スタック push pop
class stack:
    def __init__(self):
       self.items = []
        
    def is_empty(self):
       return self.items == []
        
    def push(self, item):
       self.items.append(item)
        
    def pop(self):
       return self.items.pop()
        
    def peek(self):
       return self.items[len(self.items)-1]
        
    def size(self):
       return len(self.items)

#深さ優先探索
def dfs(i, j):
    h = 0
    w = 0
    c = []
    boo = [[]]
    if h <= i or w <= j or 0 > i or 0 > j or c[i][j] == "#":
        return
    if boo[i][j] == True:
        return
    boo[i][j] = True

    dfs(i, j + 1)
    dfs(i, j - 1)
    dfs(i + 1, j)
    dfs(i - 1, j)

#幅優先探索
import queue
tf = [[]]
ans = []
voi = []
def bfs(v):
    q = queue.Queue()
    q.put([v, 0, v])
    voi[v] = True
    while not q.empty():
        sub = q.get()
        now = sub[0]
        depth = sub[1]
        before = sub[2]
        if tf[now][v] == False:
            ans[depth] += 1
            tf[now][v] = True
            tf[v][now] = True
        for next in graph[now]:
            if voi[next]:
                continue
            voi[next] = True
            q.put([next, depth + 1, now])

#二分探索
import bisect
a = [1, 3, 5, 7, 9, 11, 13, 15, 17]
x = 4
insert_index = bisect.bisect_left(a, x)
a.insert(insert_index, x)
def binary_search(a,x):
    # a=list,x=値
    left = 0
    right = len(a)
    while right - left >= 1:
        mid = (right + left) // 2
        if a[mid] == x:
            return True
        elif a[mid] > x:
            right = mid
        else:
            left = mid + 1
    return False

# graph作成
graph = {i: [] for i in range(1, n + 1)}
for _ in range(n):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

#　優先度付きキュー
import heapq
ab = []
k = 0
heapq.heapify(ab)
ans = 0
for i in range(k):
    sub = heapq.heappop(ab)
    ans += sub[0]
    sub[0] += sub[1]
    heapq.heappush(ab, sub)

#Union Find
# https://note.nkmk.me/python-union-find/
class UnionFind():
    def __init__(self, n):
        self.n = n
        self.parents = [-1] * n

    def find(self, x):
        if self.parents[x] < 0:
            return x
        else:
            self.parents[x] = self.find(self.parents[x])
            return self.parents[x]

    def union(self, x, y):
        x = self.find(x)
        y = self.find(y)

        if x == y:
            return

        if self.parents[x] > self.parents[y]:
            x, y = y, x

        self.parents[x] += self.parents[y]
        self.parents[y] = x

    def size(self, x):
        return -self.parents[self.find(x)]

    def same(self, x, y):
        return self.find(x) == self.find(y)

    def members(self, x):
        root = self.find(x)
        return [i for i in range(self.n) if self.find(i) == root]

    def roots(self):
        return [i for i, x in enumerate(self.parents) if x < 0]

    def group_count(self):
        return len(self.roots())

    def all_group_members(self):
        return {r: self.members(r) for r in self.roots()}

    def __str__(self):
        return '\n'.join('{}: {}'.format(r, self.members(r)) for r in self.roots())