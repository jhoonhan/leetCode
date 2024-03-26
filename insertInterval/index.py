class Solution:
    def insert(self, intervals: list, newInterval: list) -> list:
        intervals.append(newInterval)
        intervals.sort(key=lambda i: i[0])
        res = []
        s = intervals[0][0]
        e = intervals[0][1]
        for i in range(1, len(intervals)):
            cs = intervals[i][0]
            ce = intervals[i][1]
            if e < cs:
                res.append([s, e])
                s = cs
                e = ce
            else:
                e = max(e, ce)

        res.append([s, e])

        return res


Solution().insert([[1, 2], [3, 5], [6, 7], [8, 10], [12, 16]], [4, 8])
