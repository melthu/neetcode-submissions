class Solution:
    def isPalindrome(self, s: str) -> bool:

        cls = ""
        
        for char in s:
            if char.isalnum():
                cls = cls + char

        n = len(cls)
        lp = 0
        rp = n - 1

        while (rp > lp):
            if (cls[lp].lower() != cls[rp].lower()):
                return False

            lp += 1
            rp -= 1

        return True
        