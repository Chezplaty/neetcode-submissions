class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1

        while l < r:
            mid = (l + r)//2

            if nums[mid] > nums[mid+1]:
                return nums[mid+1]
            if nums[mid] < nums[mid+1] and nums[mid] > nums[r]:
                l = mid
            elif nums[mid] < nums[mid+1] and nums[mid] < nums[r]:
                r = mid

        
        return nums[r]
        
            