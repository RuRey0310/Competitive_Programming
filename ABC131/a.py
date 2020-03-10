s = list(input())

for i in range(3):
    if (s[i] == s[i + 1]):
        print("Bad")
        break
    if (i == 2):
        print("Good")
        break
