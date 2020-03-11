s = int(input())

cnt = [s]
while True:
    if s % 2 == 0:
        s = s // 2
    else:
        s = (3 * s) + 1
    if s in cnt:
        cnt.append(s)
        break
    else:
        cnt.append(s)

print(len(cnt))
