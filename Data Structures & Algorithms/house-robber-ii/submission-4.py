class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        if len(nums) == 2:
            return max(nums[0], nums[1])

        def dp(arr):
        
            prev, curr = arr[0], max(arr[0], arr[1])

            for i in range(2, len(arr)):
                prev, curr = curr, max(arr[i]+ prev, curr)
            
            return curr
    
        return max(dp(nums[1:]), dp(nums[:-1]))