from collections import defaultdict


class Solution:
    def canFinish(self, numCourses: int, prerequisites) -> bool:
        adj = defaultdict(list)
        for el in prerequisites:
            adj[el[0]].append(el[1])

        visited = set()

        def dfs(course):
            if course in visited:
                return False
            if adj[course] == []:
                return True

            visited.add(course)
            for preq in adj[course]:
                res = dfs(preq)
                if not res:
                    return False

            visited.remove(course)
            adj[course] = []

            return True

        for i in range(numCourses):
            if not dfs(i):
                return False

        return True


# Solution().canFinish(2, [[0, 1], [0, 2], [1, 3], [1, 4], [3, 4]])
Solution().canFinish(2, [[0, 1], [1, 0]])
