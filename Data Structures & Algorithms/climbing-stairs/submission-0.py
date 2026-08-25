class Solution:
    def climbStairs(self, n: int) -> int:
        res = 0
        saved = [None] * n
        
        #instead of adding, subtract the steps
        def add_step(i):
            if i == n:
                return 1
            
            if i > n:
                return 0
            
            if saved[i] is not None:
                return saved[i]
            
            steps = add_step(i + 1) + add_step(i+2)
            saved[i] = steps
            return steps
        
        return add_step(0)
