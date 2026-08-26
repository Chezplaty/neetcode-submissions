class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        
        saved = [None] * len(cost)
        def dfs(i):
            if i >= len(cost):
                return 0

            if saved[i] is not None:
                return saved[i]

            res = cost[i] + min(dfs(i + 1), dfs(i + 2))
            saved[i] = res
            return res

        return min(dfs(0), dfs(1))


        

        