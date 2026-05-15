#quickSelect O(n) average, but O(n^2) worse case
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        k = len(nums) - k

        l, r = 0, len(nums) - 1

        while l < r:
            pivot, p = nums[r], l

            for i in range(l, r):
                if nums[i] <= pivot:
                    nums[p], nums[i] = nums[i], nums[p]
                    p += 1
            
            nums[p], nums[r] = pivot, nums[p]

            if k < p:
                r = p - 1
            elif k > p:
                l = p + 1
            else:
                return nums[p]
                
        return nums[l]
                