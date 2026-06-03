import heapq

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        max_heap = [-s for s in stones]
        heapq.heapify(max_heap)

        while max_heap:
            if len(max_heap) == 1:
                return -max_heap[0]

            t1 = -heapq.heappop(max_heap)
            t2 = -heapq.heappop(max_heap)

            y = max(t1, t2)
            x = min(t1, t2)

            if x == y:
                continue
            else:
                heapq.heappush(max_heap, -(y - x))

        return 0

        