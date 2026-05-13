class Solution:
    def isValid(self, s: str) -> bool:

        bracket_map = { ')' : '(', '}' : '{', ']' : '['}
        stack = []

        for bracket in s:
            # if the bracket is an open bracket (not one of the keys) append it
            if bracket not in bracket_map:
                stack.append(bracket)
            else:
                #if stack does not exist, closing bracket is closing nothing
                if not stack:
                    return False
                if bracket_map[bracket] != stack[-1]:
                    return False
                stack.pop()
        
        if stack:
            return False

        return True


        