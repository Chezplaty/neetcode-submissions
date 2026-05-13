class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        max_area = 0
        stack = []

        for i, h in enumerate(heights):
            start = i
            while stack and stack[-1][1] > h:
                index, height = stack.pop()
                area = height * (i-index)
                max_area = max(max_area, area)
                start = index
            stack.append((start, h))
        
        for i, h in stack:
            area = h * (len(heights) - i)
            max_area = max(max_area, area)
        
        return max_area

