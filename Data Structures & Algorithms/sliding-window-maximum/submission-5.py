class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)

        heap = []
        for i in range(k):
            heap.append((-nums[i], i))
            
        heapq.heapify(heap)
        res = []
        res.append(-heap[0][0])

        for r in range(k, n):
            heapq.heappush(heap, (-nums[r], r))

            while heap[0][1] <= r - k:
                heapq.heappop(heap)

            res.append(-heap[0][0])
        return res


        