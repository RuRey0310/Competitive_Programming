s = list(input())

alpha = [False] * 26
for i in range(len(s)):
    alpha[ord(s[i]) - 97] = True

for i in range(len(alpha)):
    if not alpha[i]:
        print(chr(97 + i))
        break
    if i == 25:
        print("None")