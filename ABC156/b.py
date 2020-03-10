n, k = map(int, input().split())

def sinsuu(X, n):
    X_dumy = X
    out = ''
    while X_dumy>0:
        out = str(X_dumy%n)+out
        X_dumy = int(X_dumy/n)
    return out
 
ans = sinsuu(n,k)
print( len(ans) )
