class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        
        stack = []
        max_area = 0

        for i, height in enumerate(heights):
            index = i
            while stack and height <= stack[-1][0]:
                h, index = stack.pop()
                max_area = max(max_area, h*(i-index)) #i - ind --> width of that rectangle

            stack.append([heights[i], index])
        
        while stack:
            h, i = stack.pop()
            max_area = max(max_area, h * (len(heights) - i))
        
        return max_area
            