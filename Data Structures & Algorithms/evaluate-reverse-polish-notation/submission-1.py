class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for token in tokens:
            if token == '+':
                new_token = stack.pop() + stack.pop()
                stack.append(new_token)

            elif token == '-':
                second = stack.pop()
                first = stack.pop()
                new_token = first - second
                stack.append(new_token)

            elif token == '*':
                new_token = stack.pop() * stack.pop()
                stack.append(new_token)

            elif token == '/':
                second = stack.pop()
                first = stack.pop()
                new_token = first/second
                stack.append(int(new_token))

            else:
                stack.append(int(token))
        
        return stack.pop()

