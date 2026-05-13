class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l_point, r_point = 0, len(numbers) - 1

        while l_point < r_point:
            curSum = numbers[l_point] + numbers[r_point]
            if curSum > target:
                r_point -= 1
            elif curSum < target:
                l_point += 1
            
            if curSum == target:
                return [l_point + 1, r_point + 1]