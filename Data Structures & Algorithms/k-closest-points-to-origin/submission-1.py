import heapq
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        distances = []
        res = []

        for point in points:
            x, y = point
            heapq.heappush_max(distances, ((x**2 + y**2, point)))

            if len(distances) > k:
                heapq.heappop_max(distances)
            
        return [point for d, point in distances]