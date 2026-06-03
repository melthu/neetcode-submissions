class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # iterate using sliding window
        # add char to count

        # in window, check if window is valid
        # if it valid then update result and move right pointer
        # if it is not valid, move left pointer until it is valid
            
        count = dict() # char -> count
        res = 0
        l = 0

        for r in range(len(s)):
            count[s[r]] = count.get(s[r], 0) + 1
            
            while ((r  - l + 1) - max(count.values()) > k):
                count[s[l]] += -1
                l += 1
            
            res = max(res, r - l + 1)
            
        return res
                


        