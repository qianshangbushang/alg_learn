

def find_n_ugly(n:int):
    dp = [0] * n
    dp[0] = 1
    i2, i3, i5 = 0,0,0
    for idx in range(1, n):
        dp[idx] = min(dp[i2] *2, dp[i3] * 3, dp[i5] * 5)
        if dp[idx] == dp[i2] * 2:
            i2 += 1
        if dp[idx] == dp[i3] * 3:
            i3 += 1
        if dp[idx] == dp[i5] * 5:
            i5 += 1
    return dp[-1]

if __name__ == "__main__":
    print(find_n_ugly(1500))   