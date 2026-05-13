class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()

        for i, num1 in enumerate(nums):
            #Gets rid of dupes, if the next number is the same as the one before it
            #go to the next number
            if i > 0 and num1 == nums[i-1]:
                continue
            
            l, r = i + 1, len(nums) - 1
            while l < r:
                totalSum = num1 + nums[l] + nums[r]
                if totalSum > 0:
                    r -= 1
                elif totalSum < 0:
                    l += 1
                else:
                    res.append([num1, nums[l], nums[r]])
                    l += 1
                    #gets rid of dupes
                    while l < r and nums[l] == nums[l-1]:
                        l += 1
            
        return res


