class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        saved = [0] * (len(cost) + 1)

        for i in range(2, len(cost) + 1):
            saved[i] = min(saved[i - 1] + cost[i - 1],
                            saved[i - 2] + cost[i - 2])
        
        return saved[-1]