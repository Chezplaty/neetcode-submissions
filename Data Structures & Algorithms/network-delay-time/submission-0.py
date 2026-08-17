from collections import defaultdict
import heapq

class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        edgeMap = defaultdict(list)

        for u, v, t in times:
            edgeMap[u].append((t, v))
        
        minHeap = [(0, k)] #time is 0, start at node k
        res = 0
        visited = set()
        while minHeap:
            t1, n1 = heapq.heappop(minHeap)
            
            if n1 in visited:
                continue
            visited.add(n1)
            res = max(res, t1)

            for t2, adj_node in edgeMap[n1]:
                if adj_node in visited:
                    continue
                heapq.heappush(minHeap, (t2+t1, adj_node))
        
        return res if len(visited) == n else -1
