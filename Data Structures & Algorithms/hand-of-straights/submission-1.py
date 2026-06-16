class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        c = Counter(hand)
        k = list(c.keys())

        heapq.heapify(k)

        while k:
            l = k[0]
            for i in range(groupSize):
                if not c[l + i]:
                    return False
                c[l + i] += -1
                if c[l + i] == 0:
                    if k[0] == l + i:
                        heapq.heappop(k)
                    else:
                        return False

        return True
