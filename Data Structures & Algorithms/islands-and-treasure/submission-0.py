import collections

class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        row_len = len(grid)
        col_len = len(grid[0])      
        q = collections.deque()
        visited = set()

        def addCell(r, c):
            if (r < 0 or r >= row_len or c < 0 or c >= col_len
                or (r, c) in visited or grid[r][c] == -1):
                return
            visited.add((r, c)) #which chest hits the space first is the closest distance
            q.append((r, c))

        for r in range(row_len):
            for c in range(col_len):
                if grid[r][c] == 0:
                    q.append((r, c))
                    visited.add((r, c))

        dist = 0
        while q:
            #traverse level by level
            for i in range(len(q)):
                r, c = q.popleft()
                grid[r][c] = dist

                addCell(r - 1, c)
                addCell(r, c - 1)
                addCell(r + 1, c)
                addCell(r, c + 1)
            
            dist += 1
        









