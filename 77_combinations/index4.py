class Solution:
    def combine(self, n: int, k: int) -> list:
        permutes = []
        combis = []

        def permuations(acc):
            if k == len(acc):
                permutes.append(acc)
                return
            for i in range(n):
                if i not in acc:
                    prop = acc + [i]
                    permuations(prop)

        # permuations([])
        # print(permutes)

        def combination(i, acc):
            if len(acc) == k:
                combis.append(acc)
                return

            for j in range(i, n):
                combination(j + 1, acc + [j + 1])

        combination(0, [])
        print(combis)


Solution().combine(4, 2)
