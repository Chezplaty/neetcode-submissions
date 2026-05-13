class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l, r = 0, len(heights) - 1

        greatest_area = 0
        while l < r:
            right_b = heights[r]
            left_b = heights[l]
            area = (r - l) * min(right_b, left_b)
            if area > greatest_area:
                greatest_area = area
            
            #try to find a bar that is higher because only a higher height
            #can contribute to a greater area since we are decreasing the length the more we go in
            #if they are both the same, move either one (in this case, the left)
            if right_b < left_b:
                r -= 1
            else:
                l += 1
            
        return greatest_area
            