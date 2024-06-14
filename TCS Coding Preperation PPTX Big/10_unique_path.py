def uniquePaths(m, n):
    # Initialize a 2D list to store number of ways to reach each cell
    dp = [[0] * n for _ in range(m)]
    
    # Base case: There's exactly one way to be at the starting point
    dp[0][0] = 1
    
    # Fill the dp table
    for i in range(m):
        for j in range(n):
            if i > 0:
                dp[i][j] += dp[i-1][j]  # Move from top cell
            if j > 0:
                dp[i][j] += dp[i][j-1]  # Move from left cell
    
    # The answer is the number of ways to reach the bottom-right corner
    return dp[m-1][n-1]

# Example usage:
M = 5
N = 5
ways = uniquePaths(M, N)
print(f"Number of unique paths in a {M}x{N} grid: {ways}")
