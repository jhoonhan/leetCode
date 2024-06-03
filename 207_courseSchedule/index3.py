from collections import defaultdict


class Solution:
    def canFinish(self, numCourses: int, prerequisites) -> bool:
        adj_list = defaultdict(list)
        for el in prerequisites:
            adj_list[el[0]].append(el[1])

        print(adj_list)


Solution().canFinish(2, [[0, 1], [0, 2], [1, 3], [1, 4], [3, 4]])
