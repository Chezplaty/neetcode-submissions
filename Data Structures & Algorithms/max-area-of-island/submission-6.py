import collections

class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        res = 0
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        def bfs(row, col):
            q = collections.deque()
            q.append((row, col))
            grid[row][col] = 0
            area = 0
            while q:
                row, col = q.popleft()
                area += 1
                for dr, dc in directions:
                    nr, nc = row + dr, col + dc

                    if (0 <= nr < len(grid) 
                        and 0 <= nc < len(grid[0]) 
                        and grid[nr][nc] == 1
                        ):
                            grid[nr][nc] = 0
                            q.append((nr, nc))

            return area

        for r in range(len(grid)):
            for c in range(len(grid[r])):
                if grid[r][c] == 1:
                    area = bfs(r, c)
                    res = max(area, res)

        return res