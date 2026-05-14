import heapq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heapq.heapify_max(stones)


        while len(stones) > 1:

            s1 = heapq.heappop_max(stones)
            s2 = heapq.heappop_max(stones)

            diff = s1 - s2

            if diff != 0:
                heapq.heappush_max(stones, diff)
        
        if stones:
            return stones[0]

        return 0