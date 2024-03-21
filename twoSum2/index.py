class Solution:
    def twoSum(self, numbers: list, target: int) -> list:
        i = 0
        j = len(numbers) - 1
        while i < j:
            n1 = numbers[i]
            n2 = numbers[j]
            num_sum = n1 + n2
            if num_sum == target:
                print(i + 1, j + 1)

                return [i + 1, j + 1]
            elif num_sum > target:
                j -= 1
            else:
                i += 1

        return []


sol = Solution()
sol.twoSum([2, 7, 11, 15], 9)
