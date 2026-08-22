import heapq

class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        row = len(grid)
        col = len(grid[0])
        minHeap = [(grid[0][0], 0, 0)] #value, row, column
        visited = set()
        water_level = 0 #t is at least = bottom right

        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        visited.add((0, 0))
        def check_can_add(r, c):
            if (0 <= r < row and 0 <= c < col 
                and (r, c) not in visited):
                return True
            return False

        while minHeap:
            t, r, c = heapq.heappop(minHeap)
            
            if r == row - 1 and c == col - 1:
                return t

            for dr, dc in directions:
                nr = r + dr
                nc = c + dc
                if check_can_add(nr, nc):
                    # add cur water level since getting here requires being at this level
                    heapq.heappush(minHeap, (max(t, grid[nr][nc]), nr, nc))
                    visited.add((nr, nc))

        return water_level
        