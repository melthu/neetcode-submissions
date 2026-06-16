class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        n = len(gas)

        if sum(gas) < sum(cost):
            return -1

        acc = 0
        id = 0
        for i in range(n):
            acc += gas[i] - cost[i]
            if acc < 0:
                acc = 0
                id = i + 1

        return id



        