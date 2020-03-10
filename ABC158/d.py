s = input()
q = int(input())
que = [list(map(str, list(input().split()))) for i in range(q)]

hanten = 0
left = ""
right = ""
for i in range(q):
    if que[i][0] == "1":
        if hanten == 0:
            hanten = 1
        else:
            hanten = 0
    elif que[i][0] == "2":
        if hanten == 0:
            if que[i][1] == "2":
                sub = [right, que[i][2]]
                right = ''.join(sub)
            elif que[i][1] == "1":
                sub = [que[i][2], left]
                left = ''.join(sub)
        else:
            if que[i][1] == "2":
                sub = [que[i][2],left]
                left = ''.join(sub)
            elif que[i][1] == "1":
                sub = [right,que[i][2]]
                right = ''.join(sub)

sub = [left, s, right]
s = ''.join(sub)
if hanten == 1:
    s = s[::-1]
print(s)
