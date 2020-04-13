q = int(input())
lr = [list(map(int, input().split())) for i in range(q)]

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

ruiseki = [0] * MAX
for i in range(1,MAX):
    if is_prime[i]:
        if is_prime[(i + 1) // 2]:
            ruiseki[i] = ruiseki[i - 1] + 1
        else:
            ruiseki[i] = ruiseki[i - 1]
    else:
        ruiseki[i] = ruiseki[i - 1]

for i in range(q):
    print(ruiseki[lr[i][1]] - ruiseki[lr[i][0] - 1])
