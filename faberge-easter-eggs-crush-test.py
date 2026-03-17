def height(n: int, m: int) -> int:
    # Recurrence relation:
    # F(n, m) = F(n - 1, m - 1) + 1 + F(n, m - 1)
    
    if n == 0 or m == 0:
        return 0
    
    dp = [[0 for _ in range(m + 1)] for _ in range(n + 1)]
    
    for j in range(m + 1):
        dp[1][j] = j
    
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            dp[i][j] = dp[i - 1][j - 1] + 1 + dp[i][j - 1]
    
    return dp[n][m]
