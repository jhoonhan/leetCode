class Solution:
    def findKthLargest(self, nums: list, k: int) -> int:
        heap = nums[:k]
        heapify(heap)

        for i in range(k, len(nums)):
            if nums[i] > heap[0]:
                heappushpop(heap, nums[i])
        return heap[0]


Solution().findKthLargest([3, 2, 1, 5, 6, 4], 2)
