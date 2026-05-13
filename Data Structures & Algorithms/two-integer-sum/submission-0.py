class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashMap = {}

        for i, val in enumerate(nums):
            diff = target - val
            if diff in hashMap:
                return [hashMap[diff], i]
            
            hashMap[val] = i


        