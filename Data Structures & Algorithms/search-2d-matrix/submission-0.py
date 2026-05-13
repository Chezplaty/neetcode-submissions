class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        first, last = 0, len(matrix) - 1

        while first <= last:
            middle = (first+last)//2
            search_matrix = matrix[middle]
            if target < search_matrix[0]:
                last = middle - 1
            elif target > search_matrix[-1]:
                first = middle + 1
            else:
                break

        if not first <= last:
            return False
        
        l, r = 0, len(search_matrix) - 1
        while l <= r:
            mid = (l + r)//2
            if target == search_matrix[mid]:
                return True
            elif target > search_matrix[mid]:
                l = mid + 1
            elif target < search_matrix[mid]:
                r = mid - 1
        
        return False
