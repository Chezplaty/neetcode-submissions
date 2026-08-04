class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        visited = set()
        islands = 0

        def dfs(row, col):

            if grid[row][col] == '0' or (row, col) in visited:
                return 

            #if 1, keep searching for more
            visited.add((row, col))
            #go up
            if row - 1 >= 0:
                dfs(row - 1, col)
            
            #go right
            if col + 1 < len(grid[0]):
                dfs(row, col + 1)

            #go down
            if row + 1 < len(grid):
                dfs(row + 1, col)

            #go left
            if col - 1 >= 0:
                dfs(row, col - 1)
        
        for r in range(len(grid)):
            for c in range(len(grid[r])):
                #find starting point
                if grid[r][c] == '1' and (r, c) not in visited:
                    dfs(r, c) # add island after exploring all options
                    islands += 1

        return islands
