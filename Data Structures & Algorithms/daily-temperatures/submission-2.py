class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)

        stack = []

        for i in range(len(temperatures)):
            
            while stack and temperatures[i] > temperatures[stack[-1]]:
                lower_i = stack.pop()
                res[lower_i] = i - lower_i

            stack.append(i)
        
        return res