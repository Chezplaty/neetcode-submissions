class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [float('inf')] * (amount + 1)
        dp[0] = 0

        for i in range(1, amount + 1):
            for c in coins:
                diff = i - c
                if diff >= 0:
                    dp[i] = min(1 + dp[diff], dp[i])
        
        return dp[amount] if dp[amount] != float('inf') else -1