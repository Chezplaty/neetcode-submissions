#try quickselect, make distance the first index, and then point the second
# (distance, [x, y])

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        l, r = 0, len(points) - 1

        while l < r:
            p, pivot = l, points[r][0]**2 + points[r][1]**2

            for i in range(l, r):
                dist = points[i][0]**2 + points[i][1]**2
                if dist < pivot:
                    points[p], points[i] = points[i], points[p]
                    p += 1

            points[p], points[r] = points[r], points[p]

            if p == k - 1:
                return points[:k]
            elif p < k - 1:
                l = p + 1
            else:
                r = p - 1

        return points[:k]
        
        