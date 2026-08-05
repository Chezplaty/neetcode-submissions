import collections

class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        res = 0

        def bfs(row, col):
            q = collections.deque()
            q.append((row, col))
            grid[row][col] = 0
            area = 0
            while q:
                row, col = q.popleft()
                 #mark as visited
                area += 1

                if row - 1 >= 0:
                    if grid[row-1][col] == 1:
                        q.append((row-1, col))
                        grid[row-1][col] = 0
                
                if col - 1 >= 0:
                    if grid[row][col - 1] == 1:
                        q.append((row, col-1))
                        grid[row][col-1] = 0

                if row + 1 < len(grid):
                    if grid[row+1][col] == 1:
                        q.append((row+1,col))
                        grid[row+1][col] = 0
                
                if col + 1 < len(grid[row]):
                    if grid[row][col + 1] == 1:
                        q.append((row, col+1))
                        grid[row][col+1] = 0

            return area

        for r in range(len(grid)):
            for c in range(len(grid[r])):
                if grid[r][c] == 1:
                    area = bfs(r, c)
                    res = max(area, res)

        return res