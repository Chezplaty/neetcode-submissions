from collections import defaultdict

class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        
        dp = [defaultdict(int) for _ in range(len(nums) + 1)]

        dp[0][0] = 1 # value of 0, cur_sum of 0

        for i in range(len(nums)):
            for cur_sum, ways in dp[i].items():
                dp[i + 1][cur_sum + nums[i]] += ways
                dp[i + 1][cur_sum - nums[i]] += ways
        
        return dp[len(nums)][target]