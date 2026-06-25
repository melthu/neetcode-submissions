class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        freq = Counter(nums)

        counts = defaultdict(list)
        for i, count in freq.items():
            counts[count].append(i)

        sol = []
        for i in range(n):
            for num in counts[n - i]:
                sol.append(num)
            if len(sol) == k:
                return sol
