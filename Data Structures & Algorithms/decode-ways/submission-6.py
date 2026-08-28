class Solution:
    def numDecodings(self, s: str) -> int:
        nums = {str(i) for i in range(10, 27)}
        
        dp1 = 1
        dp2 = 0
        curr = 0

        for i in range(len(s) - 1, -1, -1):
            if s[i] == '0':
                curr = 0
            else:
                curr = dp1
            
            if (i + 1 < len(s) and
                (s[i] == '1' or s[i] == '2') and
                (s[i] + s[i + 1]) in nums):
                curr += dp2
            
            curr, dp1, dp2 = 0, curr, dp1
        
        return dp1