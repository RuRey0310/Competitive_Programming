#最大公約数
def gcd(a, b):
    while b!=0:
        a,b=b,a%b
    return a

#最小公倍数
def lcm(a,b):
    return a * b // gcd(a, b)
    
#sort 昇順、降順 二次元配列
a=[]
a.sort(key = lambda x: x[1])
a.sort(key = lambda x: x[1] , reverse = True)

#正の無限大,負の無限大
x = float("inf")
y = float("-inf")

#for文降順
n=0
for i in reversed(range(n + 1)): continue

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