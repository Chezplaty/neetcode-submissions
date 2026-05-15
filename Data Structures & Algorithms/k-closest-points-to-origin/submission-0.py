import heapq
import math
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        distances = []
        res = []

        for point in points:
            x, y = point
            distances.append((math.sqrt(x*x + y*y), point))
        
        heapq.heapify(distances)

        while k:
            res.append(heapq.heappop(distances)[1])
            k -= 1
        
        return res
            