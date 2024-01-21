class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        mapPS, mapSP = {}, {}
        strs = s.split()
        if len(pattern) != len(strs):
            return False
        for p, s in zip(pattern, strs):
            if (p in mapPS and mapPS[p] != s) or (s in mapSP and mapSP[s] != p):
                return False
            mapPS[p] = s
            mapSP[s] = p

        return True


Solution().wordPattern("abba", "dog cat cat fish")
