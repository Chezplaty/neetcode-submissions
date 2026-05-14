class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        length = len(nums)
        nums.sort()

        res = []
        for i, num1 in enumerate(nums):
            if num1 > 0:
                break

            if i > 0 and num1 == nums[i-1]:
                continue
            
            l, r = i + 1, len(nums) - 1
            while l < r:
                sum_nums = num1 + nums[l] + nums[r]
                
                if sum_nums == 0:
                    res.append([num1, nums[l], nums[r]])

                    l += 1
                    while l < r and nums[l] == nums[l-1]:
                        l += 1
                
                elif sum_nums > 0:
                    r -= 1

                elif sum_nums < 0:
                    l += 1

        return res      

            
            
            
            
            

                
