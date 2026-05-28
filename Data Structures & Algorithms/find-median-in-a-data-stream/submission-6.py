import heapq

class MedianFinder:

    def __init__(self):
        self.lower = [] #implement as a maxHeap (we want the max from this heap)
        self.higher = [] #implement as a minHeap (we always want the min from this heap)
        

    def addNum(self, num: int) -> None:
        heapq.heappush_max(self.lower, num)

        #check if the max element from lower is less than min element from maxHeap
        if self.higher and self.lower[0] > self.higher[0]:
            n = heapq.heappop_max(self.lower)
            heapq.heappush(self.higher, n)
        
        if len(self.lower) - len(self.higher) > 1:
            n = heapq.heappop_max(self.lower)
            heapq.heappush(self.higher, n)
        
        if len(self.higher) - len(self.lower) > 1:
            n = heapq.heappop(self.higher)
            heapq.heappush_max(self.lower, n)

    def findMedian(self) -> float:
        if len(self.lower) > len(self.higher):
            return self.lower[0]

        if len(self.lower) < len(self.higher):
            return self.higher[0]

        return (self.lower[0] + self.higher[0]) / 2

        
        