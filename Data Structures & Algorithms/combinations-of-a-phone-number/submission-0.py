class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        res, subset = [], []
        letter_map = {2: 'abc', 3: 'def', 4: 'ghi', 5: 'jkl', 6: 'mno',
                      7: 'pqrs', 8:'tuv', 9:'wxyz'}

        def backtrack(i):
            
            if i == len(digits):
                combi = "".join(subset)
                res.append(combi)
                return

            #get chars corresponding to digit
            letters = letter_map[int(digits[i])]

            for letter in letters:
                subset.append(letter)
                backtrack(i+1)
                subset.pop()
        
        backtrack(0)
        return res

        