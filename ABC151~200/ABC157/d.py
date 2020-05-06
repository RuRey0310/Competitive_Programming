class UnionFind():
    def __init__(self, n):
        self.n = n
        self.parents = [-1] * n

    def find(self, x):  #要素xが属するグループの根を返す
        if self.parents[x] < 0:
            return x
        else:
            self.parents[x] = self.find(self.parents[x])
            return self.parents[x]

    def union(self, x, y):  #要素xが属するグループと要素yが属するグループを併合
        x = self.find(x)
        y = self.find(y)

        if x == y:
            return

        if self.parents[x] > self.parents[y]:
            x, y = y, x

        self.parents[x] += self.parents[y]
        self.parents[y] = x

    def size(self, x):  #グループのサイズ
        return -self.parents[self.find(x)]

    def same(self, x, y):   #要素xと要素yが同じグループかどうか
        return self.find(x) == self.find(y)

    def members(self, x):   #要素xが属するグループに属する要素をリストで返す
        root = self.find(x)
        return [i for i in range(self.n) if self.find(i) == root]

    def roots(self):    #すべての根の要素をリストで返す
        return [i for i, x in enumerate(self.parents) if x < 0]

    def group_count(self):  #グループの数を変えす
        return len(self.roots())

    def all_group_members(self):
        return {r: self.members(r) for r in self.roots()}

    def __str__(self):
        return '\n'.join('{}: {}'.format(r, self.members(r)) for r in self.roots())

n, m, k = map(int, input().split())
friend = UnionFind(n + 1)

a, b = [], []
num = [0] * (n + 1)
for i in range(m):
    aa, bb = map(int, input().split())
    a.append(aa)
    b.append(bb)
    num[aa] += 1
    num[bb] += 1
    friend.union(aa, bb)

c,d = [],[]
for i in range(k):
    cc, dd = map(int, input().split())
    c.append(cc)
    d.append(dd)

ans = [0] * (n + 1)
for i in range(1, n + 1):
    ans[i] = friend.size(i)
    ans[i] -= num[i]
    ans[i] -= 1

for i in range(k):
    if friend.same(c[i], d[i]):
        ans[c[i]] -= 1
        ans[d[i]] -= 1

for i in range(1, n + 1):
    print(ans[i],end=" ")