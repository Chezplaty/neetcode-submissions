import heapq

class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        row = len(grid)
        col = len(grid[0])
        minHeap = [(grid[0][0], 0, 0)] #value, row, column
        visited = set()
        water_level = 0 #t is at least = bottom right

        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        def check_can_add(r, c):
            if (0 <= r < row and 0 <= c < col 
                and (r, c) not in visited):
                return True
            return False

        while minHeap:
            val, r, c = heapq.heappop(minHeap)
            visited.add((r, c))
            if val > water_level:
                water_level = val
            
            if r == row - 1 and c == col - 1:
                return water_level

            for dr, dc in directions:
                nr = r + dr
                nc = c + dc
                if check_can_add(nr, nc):
                    heapq.heappush(minHeap, (grid[nr][nc], nr, nc))
        
        return water_level
        