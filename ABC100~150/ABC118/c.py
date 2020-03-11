n = int(input())
a = list(map(int,input().split()))

def gcb(a, b):
    while b!=0:
        a,b=b,a%b
    return a

for i in range(n - 1):
    a[i + 1] = gcb(a[i], a[i + 1])
    
print(a[n - 1])
