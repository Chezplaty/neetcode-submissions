class Solution:
    def trap(self, height: List[int]) -> int:
        l, r = 0, len(height) - 1
        
        maxL = height[l]
        maxR = height[r]
        max_area = 0
        while l < r:

            if maxL <= maxR:
                l += 1
                if height[l] > maxL:
                    maxL = height[l]
                
                #dont have to check if negative because if maxL got updated, then
                #maxL and height are the same value and equal 0
                #it will only be >= 0 
                max_area += maxL - height[l]
            
            else:
                r -= 1
                water = maxR - height[r]
                if height[r] > maxR:
                    maxR = height[r]

                max_area += maxR - height[r]
        
        return max_area
            


            
            
