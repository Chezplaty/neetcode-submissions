class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1
        res = float('inf')

        while l <= r:
            mid = (l+r) // 2

            num = nums[mid]
            res = min(num, res)

            if num <= nums[r]:
                r = mid - 1
            else:
                l = mid + 1
        
        return res