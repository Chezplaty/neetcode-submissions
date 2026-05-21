class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        if len(tokens) == 1:
            return int(tokens[0])
        
        stack = []
        res = 0
        for token in tokens:

            if token == '+':
                num1 = int(stack.pop())
                num2 = int(stack.pop())
                res = num1 + num2
                stack.append(res)
            elif token == '-':
                num1 = int(stack.pop())
                num2 = int(stack.pop())
                res = num2 - num1
                stack.append(res)
            elif token == '*':
                num1 = int(stack.pop())
                num2 = int(stack.pop())
                res = num1 * num2
                stack.append(res)
            elif token == '/':
                num1 = int(stack.pop())
                num2 = int(stack.pop())
                res = num2 / num1
                stack.append(res)
            else:
                stack.append(token)
            print(stack)
        
        return int(res)
            