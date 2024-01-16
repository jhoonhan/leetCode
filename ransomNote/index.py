class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        hasmap = {}
        for i in magazine:
            if i in hasmap:
                hasmap[i] += 1
            else:
                hasmap[i] = 1

        for i in ransomNote:
            if i in hasmap and hasmap[i] > 0:
                hasmap[i] -= 1
            else:
                return False
        return True


Solution().canConstruct("aac", "aab")
