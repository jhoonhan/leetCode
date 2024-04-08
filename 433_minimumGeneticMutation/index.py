import collections


class Solution:
    def minMutation(self, startGene: str, endGene: str, bank: list) -> int:
        chars = ["A", "C", "G", "T"]

        q = collections.deque()
        q.append([startGene, 0])

        visited = set()

        while q:
            node, moves = q.popleft()

            for i in range(len(node) - 1, -1, -1):
                temp = list(node[:])
                for c2 in chars:
                    temp[i] = c2
                    val = "".join(temp)

                    if val not in bank or val in visited:
                        continue

                    if val == endGene:
                        return moves + 1

                    if val not in visited:
                        q.append([val, moves + 1])
                        visited.add(val)
        return -1


Solution().minMutation("AAAA", "AACG", ["AAAC", "AACC", "AACG"])
