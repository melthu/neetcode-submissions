class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s):
            return ""

        target = Counter(t)
        window = {}
        for c in t:
            window[c] = 0

        sol = len(s) + 1
        solstring = ""

        have = 0
        need = len(target)
        l, r = 0, 0
        while r < len(s):
            if s[r] not in target:
                r += 1
                continue

            window[s[r]] += 1
            if window[s[r]] == target[s[r]]:
                have += 1
                while have == need:
                    if sol > r - l + 1:
                        sol = r - l + 1
                        solstring = s[l:r + 1]
                    if s[l] in window:
                        window[s[l]] -= 1
                        if window[s[l]] < target[s[l]]:
                            have -= 1
                    l += 1
            r += 1
        return solstring
