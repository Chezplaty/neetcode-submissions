class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = [1]
        suffix = [1 for i in range(len(nums)+ 1)]
        for i in range(len(nums)):
            num_to_append = prefix[i] * nums[i]
            prefix.append(num_to_append)
        
        for i in range(len(nums), 0, -1):
            num = suffix[i] * nums[i-1]
            suffix[i-1] = num

        i = 0
        res = []
        while i < len(prefix) - 1:
            j = i + 1
            num_to_append = prefix[i] * suffix[j]
            res.append(num_to_append)
            i += 1

        return res
