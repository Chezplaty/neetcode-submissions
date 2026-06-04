class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        
        if len(nums) == 0:
            return [[]]
        
        perms = self.permute(nums[1:])
        res = []
        for subset in perms:
            for i in range(len(subset) + 1):
                p = subset.copy()
                p.insert(i, nums[0])
                res.append(p)
        
        return res


        


            
            