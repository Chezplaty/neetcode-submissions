class Solution:
    def partition(self, s: str) -> List[List[str]]:
        
        res, subset = [], []

        def check_palindrome(l, r):

            while l <= r:
                if s[l] != s[r]:
                    return False
                l += 1
                r -= 1
            
            return True

        def backtrack(start):

            if start == len(s):
                res.append(subset[:])
                return
            
            for end in range(start, len(s)):
                if check_palindrome(start, end):
                    subset.append(s[start : end + 1])
                    backtrack(end + 1)
                    subset.pop()
        
        backtrack(0)
        
        return res

        