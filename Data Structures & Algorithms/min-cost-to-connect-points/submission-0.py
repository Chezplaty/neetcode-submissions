import heapq

class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        manhattan = lambda p1, p2: abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])

        total_cost = 0
        visited = set()
        minHeap = [(0, points[0])] # (cost, point)

        while minHeap:
            cost, point = heapq.heappop(minHeap)

            if tuple(point) in visited:
                continue
            
            visited.add(tuple(point))
            total_cost += cost
            if len(visited) == len(points):
                return total_cost
            for p in points:
                if tuple(p) not in visited:
                    heapq.heappush(minHeap, (manhattan(point, p), p))
        
        return total_cost

