#標準入力
a = int(input())

#1 2 3 4 5...n(数字)
b = list(map(int,input().split()))

#abcde...(文字列分割して配列に入れる)
c = list(input())

#n回複数行とる
n=0
string_list = [input() for i in range(n)]
int_list = [int(input()) for i in range(n)]

#2次元配列n回
k = [list(map(int, list(input().split()))) for i in range(n)]

#a[1] b[1]
#a[n] b[n]
a, b= [0] * n, [0] * n
for i in range(n):
    a[i], b[i] = map(int, input().split())

#配列を任意の値・要素数で初期化
l = [0] * 10
#二次元配列初期化
dp = [[0] * (n + 1) for i in range(3)]

#絶対値
abs(x=1)