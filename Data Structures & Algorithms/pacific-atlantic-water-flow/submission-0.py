class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        row_len = len(heights)
        col_len = len(heights[0])

        pacific = set()
        atlantic = set()
        
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        def dfs(r, c, ocean, prevHeight):
            #check if heights[r][c] is greater than or equal to prev height
            if (r < 0 or r >= row_len or c < 0 or c >= col_len or
                (r, c) in ocean or heights[r][c] < prevHeight):
                return
            
            ocean.add((r, c))
            
            #check other directions
            for dr, dc in directions:
                nr = r + dr
                nc = c + dc

                dfs(nr, nc, ocean, heights[r][c])

        for c in range(col_len):
            dfs(0, c, pacific, heights[0][c])
            dfs(row_len - 1, c, atlantic, heights[row_len-1][c])
        
        for r in range(row_len):
            dfs(r, 0, pacific, heights[r][0])
            dfs(r, col_len -1, atlantic, heights[r][col_len-1])

        result = pacific.intersection(atlantic)
        return list(result)

        