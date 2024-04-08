import collections

"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""


class Solution:
    def cloneGraph(self, node: Optional["Node"]) -> Optional["Node"]:
        if node == None:
            return None
        hashmap = {}
        q = collections.deque([node])

        while q:
            node = q.popleft()
            if node.val not in hashmap:
                hashmap[node.val] = Node(node.val)
            else:
                continue
            for nei in node.neighbors:
                q.append(nei)

        visited = {}
        q.append(node)
        while q:
            node = q.popleft()
            if node.val not in visited:
                for nei in node.neighbors:
                    hashmap[node.val].neighbors.append(hashmap[nei.val])
                visited[node.val] = True
            else:
                continue
            for nei in node.neighbors:
                q.append(nei)

        return hashmap[1]

    def cloneGraph(self, node: Optional["Node"]) -> Optional["Node"]:
        hashmap = {}
        visited = {}

        def dfs(node):
            if node.val in visited:
                return
            else:
                visited[node.val] = True

            if node.val not in hashmap:
                hashmap[node.val] = Node(node.val)

            new_node = hashmap[node.val]
            for nei in node.neighbors:
                if nei.val not in hashmap:
                    hashmap[nei.val] = Node(nei.val)

                new_node.neighbors.append(hashmap[nei.val])

                dfs(nei)

        dfs(node)
        return hashmap[1]
