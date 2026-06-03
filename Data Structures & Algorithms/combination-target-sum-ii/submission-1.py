class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        
        res = []
        candidates.sort()
        subset = []

        def dfs(i: int, running_sum: int):
            
            if running_sum == target:
                res.append(subset.copy())
                return

            if running_sum > target or i == len(candidates):
                return
            
            # decision 1: add the number
            subset.append(candidates[i])
            dfs(i + 1, running_sum + candidates[i])

            #decision 2: dont add the number, move on
            subset.pop()

            #skip consecutive candidates
            while i + 1 < len(candidates) and candidates[i] == candidates[i+1]:
                i += 1

            dfs(i + 1, running_sum)
        
        dfs(0, 0)
        return res

