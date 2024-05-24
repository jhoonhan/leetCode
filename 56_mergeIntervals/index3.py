class Solution:
    def merge(self, intervals):
        res = []
        sorted_list = sorted(intervals, key=lambda x: x[0])

        start = sorted_list[0][0]
        end = sorted_list[0][1]

        for el in sorted_list:
            el_start = el[0]
            el_end = el[1]

            if el_start <= end:
                start = min(start, el_start)
                end = max(end, el_end)
            else:
                res.append([start, end])
                start = el_start
                end = el_end
        res.append([start, end])

        return res


Solution().merge([[1, 4], [0, 0]])
