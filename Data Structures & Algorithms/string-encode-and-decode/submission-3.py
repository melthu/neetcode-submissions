class Solution:
    def encode(self, strs: List[str]) -> str:
        res = []
        for s in strs:
            res.append(str(len(s)) + "#" + s)

        return "".join(res)

    def decode(self, s: str) -> List[str]:
        res = []
        i = 0
        while i < len(s):
            start = i
            while s[i] != "#":
                i += 1

            k = int(s[start:i])
            elem = []
            for _ in range(k):
                i += 1
                elem.append(s[i])
            res.append("".join(elem))
            i += 1
        return res
