import collections

"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional


class Solution:
    def cloneGraph(self, node: Optional["Node"]) -> Optional["Node"]:

        if node == None:
            return None

        if len(node.neighbors) == 0:
            return Node(node.val)

        hashmap = {}
        visitied = {}

        def __bfs(node):
            q = collections.deque()
            q.append(node)

            while q:
                curr = q.popleft()
                if curr.val in visitied:
                    return
                visitied[curr.val] = True

                if curr.val not in hashmap:
                    hashmap[curr.val] = Node(curr.val)

                c_curr = hashmap[curr.val]

                for n_node in curr.neighbors:

                    if n_node.val not in hashmap:
                        hashmap[n_node.val] = Node(n_node.val)

                    c_curr.neighbors.append(hashmap[n_node.val])
                    if n_node.val not in visitied:
                        q.append(n_node)

        __bfs(node)

        def __dfs(node):
            if node in hashmap:
                return hashmap[node]

            copy = Node(node.val)
            hashmap[node] = copy
            for nei in node.neighbors:
                copy.neighbors.append(__dfs(nei))
            return copy

        return hashmap[1]
