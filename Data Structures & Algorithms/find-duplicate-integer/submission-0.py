class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        length = len(nums)

        for i in range(length):
            r = length - 1
            cur_num = nums[i]

            while r > i:
                if cur_num == nums[r]:
                    return cur_num
                
                r -= 1