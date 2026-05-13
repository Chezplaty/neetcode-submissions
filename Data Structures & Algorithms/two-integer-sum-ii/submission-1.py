class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:

        checked_nums = {}

        for i in range(len(numbers)):
            num = numbers[i]
            difference = target - num
            if difference in checked_nums:
                return[checked_nums[difference], i+1]
            checked_nums[num] = i+1