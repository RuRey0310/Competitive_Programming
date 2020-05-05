s = list(input())
lens = len(s)

for i in range(lens):
    for j in range(lens - i):
        left = s[0: j + 1]
        right = s[j + 1: lens - i]
        left = ''.join(left)
        right = ''.join(right)
        if left == right and i != 0:
            print(len(left)+len(right))
            exit()
        