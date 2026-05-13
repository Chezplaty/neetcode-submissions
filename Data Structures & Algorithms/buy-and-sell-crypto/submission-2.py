class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        l, r = 0, 1
        greatest_profit = 0
        while r < len(prices):
            profit = prices[r] - prices[l]

            #if profit is negative or 0, then prices[r] is the new minimum
            #move left pointer over so buy is now prices[r]
            if profit <= 0:
                l = r
            
            r += 1

            if profit > greatest_profit:
                greatest_profit = profit

        return greatest_profit   
            

