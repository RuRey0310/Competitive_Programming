a = [int(input()) for i in range(6)]

flag = True
for i in range(4):
    for j in range(i + 1, 5):
        if a[j] - a[i] > a[5]:
            flag = False
if flag == True:
    print("Yay!")
else:
    print(":(")
