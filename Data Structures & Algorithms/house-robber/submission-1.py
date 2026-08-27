class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        if len(nums) == 2:
            return max(nums[0], nums[1])
        
        prev, before = nums[0], max(nums[0], nums[1])
        curr = None
        for i in range(2, len(nums)):
            curr = max(prev+nums[i], before)
            prev = before
            before = curr    
        
        return curr
