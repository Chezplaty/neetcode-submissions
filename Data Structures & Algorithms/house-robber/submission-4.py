class Solution:
    def rob(self, nums: List[int]) -> int:
        dp = [None] * len(nums)
        def dfs(i):
            if i == 0:
                return nums[0]
            if i == 1:
                return max(nums[0], nums[1])

            if dp[i] is not None:
                return dp[i]
            
            res = max(nums[i] + dfs(i-2), dfs(i-1))
            dp[i] = res
            return res
        
        return dfs(len(nums) - 1)