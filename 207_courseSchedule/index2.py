class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj = {i: [] for i in range(numCourses)}
        for crs, prq in prerequisites:
            adj[crs].append(prq)

        visited = set()

        def dfs(crs):
            if crs in visited:
                return False
            if adj[crs] == []:
                return True

            visited.add(crs)
            for prq in adj[crs]:
                res = dfs(prq)
                if not res:
                    return False
            visited.remove(crs)
            adj[crs] = []

            return True

        for i in range(numCourses):
            if not dfs(i):
                return False
        return True
