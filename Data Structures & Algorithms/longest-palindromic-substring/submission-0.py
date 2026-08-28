class Solution:
    def longestPalindrome(self, s: str) -> str:
        res = ''
        def helper(l, r):
            
            while l >= 0 and r < len(s) and s[l] == s[r]:
                l -= 1
                r += 1
            
            return s[l + 1: r]

        for i in range(len(s)):
            #even length
            res1, res2 = helper(i, i), helper(i, i + 1)

            if len(res1) > len(res):
                res = res1
            if len(res2) > len(res):
                res = res2
        
        return res