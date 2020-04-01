mod = 10**9+7
def main():
    N,S,K = map(int,input().split())
    dp = [[0 for _ in range(S+1)] for _ in range(N)]
    dp[0][0] = 1
    for i in range(N):
        for j in range(S+1):
            if j >= N-i:
                dp[i][j] += dp[i][j-N+i]%mod
            if j >= K*(N-i):
                dp[i][j] += dp[i-1][j-K*(N-i)]%mod
    print(dp[-1][-1]%mod)
if __name__ == '__main__':
    main()