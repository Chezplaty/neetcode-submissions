class Solution:
    def isValid(self, s: str) -> bool:

        brackets = {'{' : '}', '[' :']', '(' : ')'}
        stack = []

        for bracket in s:
            
            if bracket in brackets:
                stack.append(bracket)
            
            elif not stack or bracket != brackets[stack.pop()]:
                return False
        
        return not stack
        