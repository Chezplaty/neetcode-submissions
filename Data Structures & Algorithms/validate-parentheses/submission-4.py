class Solution:
    def isValid(self, s: str) -> bool:
        bracket_map = { ')' : '(', '}' : '{', ']' : '['}
        stack = []

        for bracket in s:
            # if the bracket is a closing bracket (one of the keys)
            if stack and bracket in bracket_map:
                if stack[-1] == bracket_map[bracket]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(bracket)
                
        if stack:
            return False
        return True


        