from collections import defaultdict


class Solution:
    def findOrder(self, numCourses: int, prerequisites):
        adj = defaultdict(list)
        for el in prerequisites:
            adj[el[0]].append(el[1])

        res = []
        visit = set()
        cycle = set()

        def dfs(crs):
            if crs in cycle:
                return False
            if crs in visit:
                return True

            cycle.add(crs)
            for pre in adj[crs]:
                if not dfs(pre):
                    return False
            cycle.remove(crs)
            visit.add(crs)
            res.append(crs)
            return True


Solution().findOrder(2, [[1, 0], [2, 0], [3, 1], [3, 2]])
