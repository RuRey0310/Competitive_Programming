import collections
import copy
n = int(input())
aa = list(map(int, input().split()))

def comb(n, k):
    p = (10 ** 9) + 7
    """power_funcを用いて(nCk) mod p を求める"""
    from math import factorial
    if n<0 or k<0 or n<k: return 0
    if n==0 or k==0: return 1
    a=factorial(n) %p
    b=factorial(k) %p
    c=factorial(n-k) %p
    return (a*power_func(b,p-2,p)*power_func(c,p-2,p))%p
def power_func(a,b,p):
    """a^b mod p を求める"""
    if b==0: return 1
    if b%2==0:
        d=power_func(a,b//2,p)
        return d*d %p
    if b%2==1:
        return (a * power_func(a, b - 1, p)) % p   

memo = {}
for i in range(len(aa)):
    if not aa[i] in memo:
        hu = copy.deepcopy(aa)
        del hu[i]
        a = collections.Counter(hu)
        summ = 0
        for j in a:
            summ += comb(a[j], 2)
        memo[aa[i]] = summ
    print(memo[aa[i]])
