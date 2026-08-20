from collections import defaultdict
import heapq
class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        edgeMap = defaultdict(list)
        for a, b, t in times:
            edgeMap[a].append((t, b))
        
        minHeap = [(0, k)]
        res = 0
        visited = set()

        while minHeap:
            t1, n1 = heapq.heappop(minHeap)

            if n1 in visited:
                continue
                
            res = max(res, t1)
            visited.add(n1)
            for t2, n2 in edgeMap[n1]:
                if n2 not in visited:
                    heapq.heappush(minHeap, (t2 + t1, n2))

        if len(visited) == n:
            return res
        
        return -1
        

