class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        start, end = newInterval

        res = []
        for i in range(len(intervals)):
            interval = intervals[i]
            if end < interval[0]:
                res.append([start, end])
                return res + intervals[i:]
            elif start > interval[1]:
                res.append(interval)
            else:
                start = min(start, interval[0])
                end = max(end, interval[1])

        res.append([start, end])
        return res


        