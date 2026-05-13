class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l = 1
        r = max(piles)

        
        min_k = r

        while l <= r:
            k = (l + r)//2
            hours = 0
            for pile in piles:
                hours += math.ceil(pile/k)
            
            if hours <= h:
                r = k - 1
                min_k = min(k, min_k)

            elif hours > h:
                l = k + 1
        
        return min_k
            
