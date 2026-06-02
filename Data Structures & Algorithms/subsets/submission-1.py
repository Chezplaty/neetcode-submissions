class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        
        res = []

        subset = []

        def dfs(i):

            if i >= len(nums):
                res.append(subset.copy())
                return

            # decision 1, add the number
            subset.append(nums[i])
            dfs(i + 1)

            #decision 2, do not add number
            subset.pop()
            dfs(i + 1)

        dfs(0)
        return res