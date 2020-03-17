n = int(input())
w = [int(input()) for i in range(n)]

box = [w[0]]
for i in range(1,n):
    for j in range(len(box)):
        if w[i] <= box[j]:
            box[j] = w[i]
            break
        if j == len(box) - 1:
            box.append(w[i])
    box.sort()

print(len(box))