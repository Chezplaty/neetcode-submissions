class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = [[]]
        
        def dfs(index):
            
            if index >= len(nums):
                return

            cur_num = nums[index]
            new = []
            for subset in res:
                new_sub = subset[::]
                new_sub.append(cur_num)
                new.append(new_sub)
            
            res.extend(new)
            
            dfs(index + 1)

        dfs(0)
        return res

