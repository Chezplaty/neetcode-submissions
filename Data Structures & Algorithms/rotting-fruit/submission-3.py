from collections import deque

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:

        q = deque()
        fresh_fruits = 0

        row_len = len(grid)
        col_len = len(grid[0])

        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]

        for r in range(row_len):
            for c in range(col_len):
                if grid[r][c] == 2:
                    q.append((r, c))
                elif grid[r][c] == 1:
                    fresh_fruits += 1

        mins = 0
        while q and fresh_fruits > 0:

            for i in range(len(q)):
                row, col = q.popleft()

                for dr, dc in directions:
                    nr = row + dr
                    nc = col + dc

                    if (0 <= nr < row_len and
                        0 <= nc < col_len and
                        grid[nr][nc] == 1):

                        grid[nr][nc] = 2
                        fresh_fruits -= 1
                        q.append((nr, nc))

            mins += 1
        return mins if fresh_fruits == 0 else -1





