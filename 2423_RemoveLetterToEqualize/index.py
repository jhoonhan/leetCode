class Solution:
    def equalFrequency(self, word: str) -> bool:
        hashmap = {}
        for c in word:
            if c not in hashmap:
                hashmap[c] = 1
                continue
            hashmap[c] += 1

        vals = list(set(hashmap.values()))

        if len(vals) > 2 or len(vals) == 1:
            return False

        disc = abs(vals[0] - vals[1])
        if disc > 1:
            return False
        else:
            return True


Solution().equalFrequency("aacc")
