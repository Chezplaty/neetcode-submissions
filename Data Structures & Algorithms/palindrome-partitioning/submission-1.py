class Solution:
    def partition(self, s: str) -> List[List[str]]:
        
        res, subset = [], [s[0]]
        if len(s) == 1:
            return [subset]

        #i - keeps track of letter to add
        def backtrack(i):

            #check if everything is a palindrome
            if i == len(s):
                if self.check_palindrome(subset):
                    res.append(subset[:])
                return

            # add character to current string
            subset[-1] += s[i]
            backtrack(i+1)

            #remove last character
            if len(subset[-1]) > 1:
                subset[-1] = subset[-1][:-1]
            else:
                subset.pop()

            #append character to subset
            subset.append(s[i])
            backtrack(i+1)
            subset.pop()

        backtrack(1)
        return res
    
    def check_palindrome(self, subset: list[str]):
        for substr in subset:
            l, r = 0, len(substr) - 1

            while l <= r:
                if substr[l] != substr[r]:
                    return False
                l += 1
                r -= 1
        
        return True

