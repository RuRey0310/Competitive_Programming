n, k = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
c = list(map(int, input().split()))

done = [[0] * (n + 1) for i in range(k + 1)]
memo = [[0] * (n + 1) for i in range(k + 1)]

def search(i, u):
    if done[i][u]:
        return memo[i][u]
    
    if i == n:
        return 0
        
