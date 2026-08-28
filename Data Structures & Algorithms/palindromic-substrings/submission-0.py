class Solution:
    def countSubstrings(self, s: str) -> int:
        
        total = 0

        def helper(l, r):
            count = 0
            while l > -1 and r < len(s) and s[r] == s[l]:
                count += 1
                l -= 1
                r += 1
            
            return count
        
        for i in range(len(s)):
            total += helper(i, i)
            total += helper(i, i + 1)
        
        return total

