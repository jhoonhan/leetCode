class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        map = {}
        if len(s) != len(t):
            return False
        for i in range(len(s)):
            if s[i] in map:
                map[s[i]] += 1
            else:
                map[s[i]] = 1

        for i in range(len(t)):
            if t[i] in map and map[t[i]] > 0:
                map[t[i]] -= 1
            else:
                print(f"Failed on {t[i]}")
                return False

        return True


Solution().isAnagram("ab", "a")
