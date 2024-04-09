class Solution:
    # def reverseBits(self, n: int) -> int:
    #     res = 0
    #     str_nums = str(format(n, "032b"))

    #     for i in range(len(str_nums)):

    #         num = int(str_nums[i])
    #         val = 2**i * num
    #         # print(val)

    #         res += val
    #     # print(res)
    #     return res

    def reverseBits(self, n: int) -> int:
        out = 0
        for i in range(32):
            out *= 2
            if n % 2:
                out += 1
            n = int(n / 2)
        return out


Solution().reverseBits(43261596)
