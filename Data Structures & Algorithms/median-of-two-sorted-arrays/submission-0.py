class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        a, b = nums1, nums2
        total = len(nums1) + len(nums2)
        half = total//2

        if len(b) < len(a):
            a, b = b, a        

        l, r = 0, len(a) - 1

        while True:
            mid = (l+r)//2

            x = half - mid - 2

            Aleft = a[mid] if mid >= 0 else float("-inf")
            Aright = a[mid + 1] if mid + 1 < len(a) else float("inf")
            Bleft = b[x] if x >= 0 else float("-inf")
            Bright = b[x+1] if x + 1 < len(b) else float("inf")

            if Aleft <= Bright and Bleft <= Aright:

                if total % 2 != 0:
                    return min(Aright, Bright)
                else:
                    return (max(Aleft, Bleft) + min(Aright, Bright))/2
            
            elif Aleft > Bright:
                r = mid - 1
            
            else:
                l = mid + 1



