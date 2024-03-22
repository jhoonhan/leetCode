class Solution:
    def merge(self, intervals: list) -> list:
        intervals.sort(key=lambda i: i[0])
        start = intervals[0][0]
        end = intervals[0][1]
        res = []
        for i in range(1, len(intervals)):
            new_start = intervals[i][0]
            new_end = intervals[i][1]
            if new_start <= end:
                end = max(end, new_end)
            else:
                res.append([start, end])
                start = new_start
                end = new_end
        res.append([start, end])

        return res


Solution().merge([[1, 3], [2, 6], [8, 10], [9, 18]])
