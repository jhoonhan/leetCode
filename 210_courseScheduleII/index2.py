from collections import defaultdict


class Solution:
    def findOrder(self, numCourses: int, prerequisites):
        adj = defaultdict(list)
        for el in prerequisites:
            adj[el[0]].append(el[1])

        visitied = set()
        loop = set()

        res = []

        def dfs(crs):
            if crs in loop:
                return False
            if crs in visitied:
                return True

            loop.add(crs)
            for preq in adj[crs]:
                if not dfs(preq):
                    return False
            loop.remove(crs)

            visitied.add(crs)
            res.append(crs)
            return True

        for i in range(numCourses):
            if not dfs(i):
                return []

        return res


Solution().findOrder(4, [[1, 0], [2, 0], [3, 1], [3, 2]])
