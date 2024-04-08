import heapq


class Solution:
    def kSmallestPairs(self, nums1: list, nums2: list, k: int) -> list:
        res = []

        # Init heap. Add starting point
        heap = []
        heapq.heapify(heap)
        starting = (nums1[0] + nums2[0], (0, 0))
        heapq.heappush(heap, starting)

        # Hashset to prevent duplicate
        visited = set()

        # Iteration
        while heap and k:
            # Get the smallest combination
            val, (i, j) = heapq.heappop(heap)
            # Add to res
            res.append([nums1[i], nums2[j]])

            if i + 1 < len(nums1) and (i + 1, j) not in visited:
                item = (nums1[i + 1] + nums2[j], (i + 1, j))
                heapq.heappush(heap, item)
                visited.add((i + 1, j))
            if j + 1 < len(nums2) and (i, j + 1) not in visited:
                item = (nums1[i] + nums2[j + 1], (i, j + 1))
                heapq.heappush(heap, item)
                visited.add((i, j + 1))

            # Since we push 2 nodes per iteration, ie 2 smallest WILL be in the 4 + 1 combinations (a1, b1), (a1, b2), (a2, b1), (a2, b2), (a2, b3)
            k -= 1
        print(res)
        return res


Solution().kSmallestPairs([1, 7, 11], [2, 4, 6], 3)
