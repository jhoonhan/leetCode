class Solution:
    def merge(self, nums1, m: int, nums2, n: int) -> None:
        i = m - 1
        j = n - 1
        p = n + m - 1
        while i >= 0 and j >= 0:

            n1 = nums1[i]
            n2 = nums2[j]

            if n1 < n2:
                nums1[p] = n2
                j -= 1
            else:
                nums1[p] = n1
                i -= 1

            p -= 1
        while j >= 0:
            nums1[p] = nums2[j]
            j -= 1
            p -= 1


sol = Solution()

sol.merge([0], 0, [1], 1)
