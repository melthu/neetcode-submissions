class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1

        if n == 2:
            return 2

        one, two = 2, 1

        for i in range(3, n + 1):
            curr = one + two
            two = one
            one = curr

        return curr