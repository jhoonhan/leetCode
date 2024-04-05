class Solution:
    def findMinArrowShots(self, points: list) -> int:
        arr = sorted(points, key=lambda x: x[0])
        count = 1
        # [[1,6], [2,8], [7,12], [10,16]]
        acc = arr[0]
        for i in range(len(arr)):
            curr = arr[i]
            if curr[0] <= acc[1]:
                acc[1] = min(acc[1], curr[1])
                print("match")

            else:
                count += 1
                acc = curr
                print("bam")

        return count


Solution().findMinArrowShots([[10, 16], [2, 8], [1, 6], [7, 12]])
