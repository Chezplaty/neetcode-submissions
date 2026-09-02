class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        
        # borders < 0 < 0 >= m >= n
        #m is number of rows
        # n is columns

        dp = [[0] * n for _ in range(m)]
        dp[0][0] = 1
        for i in range(m):
            for j in range(n):
                if i == j == 0:
                    continue
                
                val = 0
                if i > 0: # in bounds
                    val += dp[i-1][j]
                if j > 0:
                    val += dp[i][j-1]
                dp[i][j] = val

        return dp[m-1][n-1]

