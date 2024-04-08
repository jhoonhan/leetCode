class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:

        adj = {i: [] for i in range(numCourses)}
        for crs, prq in prerequisites:
            adj[crs].append(prq)

        visit = set()

        res = []

        def dfs(crs):
            print(crs)

            nonlocal res
            if crs in res:
                return True

            if crs in visit:
                return False

            if adj[crs] == []:
                if crs not in res:
                    res.append(crs)
                return True

            visit.add(crs)
            for prq in adj[crs]:
                if not dfs(prq):
                    return False

            if crs not in res:
                res.append(crs)

            visit.remove(crs)
            adj[crs] = []
            return True

        for i in range(numCourses):
            if not dfs(i):
                return []

        return res

    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        prereq = {i: [] for i in range(numCourses)}
        for crs, prq in prerequisites:
            prereq[crs].append(prq)

        res = []
        visit, cycle = set(), set()

        def dfs(crs):
            if crs in cycle:
                return False
            if crs in visit:
                return True

            cycle.add(crs)
            for pre in prereq[crs]:
                if not dfs(pre):
                    return False

            cycle.remove(crs)
            visit.add(crs)
            res.append(crs)
            return True

        for c in range(numCourses):
            if not dfs(c):
                return []
        return res
