class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        if len(nums) == 2:
            return max(nums[0], nums[1])

        def dp(start, end):
        
            prev, curr = nums[start], max(nums[start], nums[start+1])

            for i in range(start+2, end):
                prev, curr = curr, max(nums[i]+ prev, curr)
            
            return curr
    
        return max(dp(1, len(nums)), dp(0, len(nums) - 1))