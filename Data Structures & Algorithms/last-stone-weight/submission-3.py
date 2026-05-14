import heapq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heapq.heapify_max(stones)
        length = len(stones)

        while length > 1:

            s1 = heapq.heappop_max(stones)
            s2 = heapq.heappop_max(stones)
            length -= 2

            diff = s1 - s2

            if diff != 0:
                heapq.heappush_max(stones, diff)
                length += 1
        
        if stones:
            return stones[0]

        return 0