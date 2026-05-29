class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        row_len, col_len = len(matrix), len(matrix[0])

        l, r = 0, row_len * col_len - 1 #act like 2D matrix is 1D (flatten it)

        while l <= r:

            mid = (l + r) // 2

            #convert the 1D mid index into 2D matrix index
            row = mid // col_len
            col = mid % col_len

            if matrix[row][col] == target:
                return True
            
            elif matrix[row][col] > target:
                r = mid - 1
            
            elif matrix[row][col] < target:
                l = mid + 1
        
        return False