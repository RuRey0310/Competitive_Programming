s = list(input())

s1 = int(s[0]) * 10 + int(s[1])
s2 = int(s[2]) * 10 + int(s[3])

if(s1 > 12 and s2 > 12):
    print("NA")
elif(s1 < 13 and s2 < 13 and s1 > 0 and s2 > 0):
    print("AMBIGUOUS")
elif(s1 < 13 and s1 > 0):
    print("MMYY")
elif(s2 > 0):
    print("YYMM")
else:
    print("NA")
