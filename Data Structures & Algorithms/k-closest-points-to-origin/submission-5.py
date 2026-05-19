#try quickselect, make distance the first index, and then point the second
# (distance, [x, y])

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        l, r = 0, len(points) - 1

        res = []
        for x, y in points:
            res.append((x**2 + y**2, [x, y]))
        
        while l < r:
            p, pivot = l, res[r][0]

            for i in range(l, r):
                if res[i][0] < pivot:
                    res[p], res[i] = res[i], res[p]
                    p += 1

            res[p], res[r] = res[r], res[p]       

            if k - 1 < p:
                r = p - 1
            elif k - 1 > p:
                l = p + 1
            else:
                return [point for d, point in res[:k]]

        return [point for d, point in res[:k]]
        
        