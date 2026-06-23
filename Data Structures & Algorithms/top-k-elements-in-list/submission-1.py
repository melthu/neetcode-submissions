class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = dict()     # num -> count
        for num in nums:
            counts[num] = counts.get(num, 0) + 1

        freq = defaultdict(list)      # count -> numbers[]
        for num in counts.keys():
            freq[counts[num]].append(num)
            
            
            
        
        result = []
        for i in range(len(nums)):
            bucket = freq.get(len(nums) - i, [])
            for num in bucket:
                result.append(num)
                if len(result) == k:
                    return result
        
        return result