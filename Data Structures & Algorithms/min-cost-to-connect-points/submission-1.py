class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        manhattan = lambda p1, p2: abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])

        n = len(points)
        total_cost = 0
        min_dist = [float('inf') for _ in range(n)]
        visited = set()
        min_dist[0] = 0 # set the first point as the start (no cost)
        for _ in range(n):

            curr = -1
            for i in range(n): #find the next minimum dist
                if i not in visited:
                    if curr == -1 or (min_dist[i] < min_dist[curr]):
                        curr = i
            
            total_cost += min_dist[curr]
            visited.add(curr)

            for i in range(n): #update minimum distance from this point
                if i not in visited:
                    min_dist[i] = min(min_dist[i], manhattan(points[curr], points[i]))
        
        return total_cost



