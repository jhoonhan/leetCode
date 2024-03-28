class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []

        # n = 1,2,3,4
        def backtrack(i, acc):
            # 0, ""
            ## 1, "1"
            ### 2, "12"
            ### 3, "13"
            ### 4, "14"
            ## 2, "2"
            ### 3, "23"
            ### 4, "24"
            ## 3, "3"
            ### 4, "34"
            ## 4, "4"
            if len(acc) == k:
                # none
                ## none
                ### res = [12]
                ### res = [12, 13]
                ### res = [12, 13, 14]
                ## none
                ### res = [12, 13, 14, 23]
                ### res = [12, 13, 14, 23, 24]
                ## none
                ### res = [12, 13, 14, 23, 24, 34]
                ## none
                res.append(acc.copy())
                return
            for j in range(i, n):
                # i=0, ['1, 2, 3, 4], ""
                ## i=1, ['2, 3, 4], "1"
                ### return "12"
                ## i=1, [2, '3, 4], "1"
                ### return "13"
                ## i=1, [2, 3, '4], "1"
                ### return "14"
                # i=1, [1, '2, 3, 4], ""
                ## i=2, ['3, 4], "2"
                ### return "23"
                ## i=2, [3, '4], "2"
                ### return "24"
                # i=2, [1, 2, '3, 4], ""
                ## i=3, ['4], "3"
                ### return "34"
                # i=3, [1, 2, 3, '4], ""
                ## i=4, [], "4"
                # END
                backtrack(j + 1, acc + [j + 1])

        backtrack(0, [])
        print(res)
        return res
