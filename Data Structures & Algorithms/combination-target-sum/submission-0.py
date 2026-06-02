class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        
        res = []
        
        subset = []

        def dfs(i, running_sum):
            if running_sum == target:
                res.append(subset.copy())
                return

            if i >= len(nums) or running_sum > target:
                return

            # Decision 1: use the same number
            subset.append(nums[i])
            dfs(i, running_sum + nums[i])
            
            # Decision 2: use a different number
            subset.pop()
            dfs(i + 1, running_sum)
        
        dfs(0, 0)

        return res
