class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        l, r = 0, 1
        greatest_profit = 0
        while r < len(prices):
            profit = prices[r] - prices[l]

            #if profit is negative or 0, then prices[r] is the new minimum
            #move both pointers over
            if profit <= 0:
                l = r
                r += 1  

            #if profit is positive, move only the right pointer to see if
            #we can reach a higher profit 
            else:
                r +=1

            if profit > greatest_profit:
                greatest_profit = profit

        return greatest_profit   
            

