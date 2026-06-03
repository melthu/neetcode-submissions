class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        max_heap = [-num for num in nums]
        heapq.heapify(max_heap)
        result = 0
        for i in range(k):
            result = -heapq.heappop(max_heap)
        return result 