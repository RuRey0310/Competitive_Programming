n = int(input())

dp = ["No"] * 101
dp[4] = "Yes"
dp[7] = "Yes"
for i in range(8, 101):
    if dp[i - 4] == "Yes":
        dp[i] = "Yes"
    elif dp[i - 7] == "Yes":
        dp[i] = "Yes"

print(dp[n])
