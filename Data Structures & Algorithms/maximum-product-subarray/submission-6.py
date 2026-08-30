class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        max_prod = nums[0]
        min_prod = nums[0]

        res = max_prod

        for i in range(1, len(nums)):
            old_max = max_prod
            old_min = min_prod

            max_prod = max(nums[i], old_max * nums[i], old_min * nums[i])
            min_prod = min(nums[i], old_max * nums[i], old_min * nums[i])
            if max_prod > res:
                print(max_prod, res)
                res = max_prod
        
        return res
            