class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 2:
            return n

        results = [1, 2]
        
        for i in range(3, n + 1):
            results.append(results[-2] + results[-1])
        
        return results[-1]