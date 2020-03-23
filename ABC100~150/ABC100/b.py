d, n = map(int, input().split())

ten = [1, 100, 10000]

sub = (n - 1) // 99
print(((100 * sub) + n - (99 * sub)) * ten[d])