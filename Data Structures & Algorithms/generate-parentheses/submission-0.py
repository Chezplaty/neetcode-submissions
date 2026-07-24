class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        
        res, subset = [], ['(']

        def backtrack(l_count, r_count):
            #full parenthesis is n*2
            if len(subset) == n * 2:

                #the last element should be a closing paren
                if subset[-1] == ')' and l_count == r_count:
                    paren = "".join(subset)
                    res.append(paren)
                return
            
            #valid to add '('
            if l_count < n:
                subset.append('(')
                l_count += 1
                backtrack(l_count, r_count)

                #return
                subset.pop()
                l_count -= 1
            
            #valid to add ')'
            if r_count < l_count:
                subset.append(')')
                r_count += 1
                backtrack(l_count, r_count)
                subset.pop()
                r_count -= 1
        
        
        backtrack(1, 0)
        return res
