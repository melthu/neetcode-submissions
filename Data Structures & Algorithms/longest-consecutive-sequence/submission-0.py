class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        chains = defaultdict(int)
        longest = 0

        for num in nums:
            if chains[num] != 0:
                continue

            chain_length = chains[num-1] + chains[num+1] + 1
            chains[num] = chain_length
            chains[num - chains[num-1]] = chain_length
            chains[num + chains[num+1]] = chain_length

            longest = max(longest, chain_length)

        return longest


        
        
        