n = int(input())
a = int(input())

ans = n % 500
if ans <= a:
    print("Yes")
else:
    print("No")