a,b = map(int,input().split())

#最大公約数
def gcb(a,b):
    while b!=0:
        a,b=b,a%b
    return a
#最小公倍数
def lcm(a,b):
    return a * b // gcb(a, b)
    
print(lcm(a,b))
