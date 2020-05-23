n = int(input())
s = [list(input()) for i in range(5)]

suuzi = ["####.##.##.####", ".#.##..#..#.###", "###..#####..###", "###..####..####"
, "#.##.####..#..#", "####..###..####", "####..####.####", "###..#..#..#..#", "####.#####.####"
, "####.####..####"]
ans = ""
for i in range(1, n * 4 -2, 4):
    sub = ""
    for j in range(5):
        for k in range(i,i+3):
            sub += s[j][k]
    for l in range(10):
        if sub == suuzi[l]:
            ans += str(l)
            break

print(ans)