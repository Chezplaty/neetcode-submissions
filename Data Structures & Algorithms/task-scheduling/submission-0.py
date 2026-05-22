from collections import Counter, deque
import heapq

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        
        counts = Counter(tasks)

        maxHeap = [cnt for cnt in counts.values()]
        heapq.heapify_max(maxHeap)

        time = 0
        q = deque()

        while maxHeap or q:
            if maxHeap:
                count = heapq.heappop_max(maxHeap) - 1
                if count > 0:
                    q.append((count, time + n))
            
            if q and q[0][1] == time:
                heapq.heappush_max(maxHeap, q.popleft()[0])
                
            time += 1
        
        return time
