class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        dp = {} # (i, buy/not buy)

        def dfs(i, buy):
            if i >= len(prices):
                return 0
            
            if (i, buy) in dp:
                return dp[(i, buy)]
            
            cooldown = dfs(i + 1, buy)

            if buy:
                val = dfs(i + 1, not buy) - prices[i]
            else:
                val = dfs(i + 2, not buy) + prices[i]
            
            dp[(i, buy)] = max(val, cooldown)
            return dp[(i, buy)]
        
        return dfs(0, True)