class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        for row in matrix:
            l, r = 0, len(row)- 1
            if target > row[r]:
                continue
            
            while l <= r:
                mid = (l+r)//2

                if row[mid] == target:
                    return True
                
                elif row[mid] > target:
                    r = mid - 1
                
                elif row[mid] < target:
                    l = mid + 1
            
            return False
        
        return False
