class MedianFinder:

    def __init__(self):
        self.lower = []
        self.upper = []

    def addNum(self, num: int) -> None:
        if not self.lower:
            heapq.heappush(self.lower, -num)
            return
        
        if not self.upper:
            if num >= -self.lower[0]:
                heapq.heappush(self.upper, num)
            else:
                heapq.heappush(self.upper, -heapq.heappop(self.lower))
                heapq.heappush(self.lower, -num)
            return

        if -self.lower[0] <= num <= self.upper[0]:
            if len(self.lower) == len(self.upper):
                heapq.heappush(self.lower, -num)
                return
            else:
                heapq.heappush(self.upper, num)
                return
        
        if num > self.upper[0]:
            if len(self.lower) == len(self.upper):
                heapq.heappush(self.lower, -heapq.heappop(self.upper))
                heapq.heappush(self.upper, num)
                return
            else:
                heapq.heappush(self.upper, num)
                return
        
        if num < -self.lower[0]:
            if len(self.lower) == len(self.upper):
                heapq.heappush(self.lower, -num)
                return
            else:
                heapq.heappush(self.upper, -heapq.heappop(self.lower))
                heapq.heappush(self.lower, -num)
                return

    def findMedian(self) -> float:
        if len(self.lower) == len(self.upper):
            return (-self.lower[0] + self.upper[0]) / 2
        else:
            return (-self.lower[0])
        
        