class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        dp = {}
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        def dfs(i, j):
            if i >= len(matrix) or j >= len(matrix[0]):
                return 0
            
            if (i, j) in dp:
                return dp[(i, j)]
            
            count = 1
            for dr, dc in directions:
                nr, nc = i + dr, j + dc
                if 0 <= nr < len(matrix) and 0 <= nc < len(matrix[0]) and matrix[nr][nc] > matrix[i][j]:
                    count = max(count, 1 + dfs(nr, nc))

            dp[(i, j)] = count
            return count 

        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                dfs(i, j)

        return max(dp.values())       

            