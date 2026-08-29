class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [None] * (amount + 1)
        dp[0] = 0

        def dfs(i):

            if dp[i] is not None:
                return dp[i]
            
            res = float('inf')
            for c in coins:
                diff = i - c
                if diff >= 0:
                    res = min(res, 1 + dfs(diff))

            dp[i] = res
            return res
        
        res = dfs(amount)
        return res if res != float('inf') else -1