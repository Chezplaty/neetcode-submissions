class Solution:
    def isValid(self, s: str) -> bool:

        brackets = {'{' : '}', '[' :']', '(' : ')'}
        stack = []

        for bracket in s:
            
            if bracket in brackets:
                stack.append(bracket)
            
            else:
                if not stack:
                    return False
                
                left_brack = stack.pop()
                if bracket != brackets[left_brack]:
                    return False
        
        if stack:
            return False
        
        return True
        