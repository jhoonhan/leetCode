import collections


class Solution:
    def calcEquation(
        self, equations: List[List[str]], values: List[float], queries: List[List[str]]
    ) -> List[float]:
        # Create adj list
        # a | (b, 2)
        # b | (a, 1/2), (c, 3)
        # c | (b, 1/3)
        adj = collections.defaultdict(list)
        for i, eq in enumerate(equations):
            el1, el2 = eq
            adj[el1].append([el2, values[i]])
            adj[el2].append([el1, 1 / values[i]])

        def bfs(src, target):
            # If any variable is not given, immediately return -1
            if src not in adj or target not in adj:
                return -1

            q = collections.deque()
            visit = set()
            # Why 1? start with 1 because anything muliplied by 1 is same
            q.append([src, 1])
            visit.add(src)
            while q:
                n, w = q.popleft()
                if n == target:
                    return w
                for nei, weight in adj[n]:
                    if nei not in visit:
                        q.append([nei, w * weight])
                        visit.add(nei)
            return -1

        return [bfs(q[0], q[1]) for q in queries]
