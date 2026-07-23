class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        
        nums.sort()
        res, subset = [], []

        def backtrack(i):
            
            if i >= len(nums):
                res.append(subset[:])
                return
            
            #include the number
            subset.append(nums[i])
            backtrack(i + 1)

            #exclude the number and no duplicates
            subset.pop()
            i += 1
            while i < len(nums) and nums[i] == nums[i - 1]:
                i += 1
            backtrack(i)
        
        backtrack(0)
        return res