import collections


class Solution:
    def equalFrequency(self, word: str) -> bool:
        cnt = collections.Counter(collections.Counter(word).values())
        print(cnt)

        if len(cnt) == 1:
            res = list(cnt.keys())[0] == 1 or list(cnt.values())[0] == 1
            print(res)

            return res
        if len(cnt) == 2:
            f1, f2 = min(cnt.keys()), max(cnt.keys())
            return (f1 + 1 == f2 and cnt[f2] == 1) or (f1 == 1 and cnt[f1] == 1)
        return False


Solution().equalFrequency("aacc")
