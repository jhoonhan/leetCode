class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hmap = {}

        for char in s:
            if char not in hmap:
                hmap[char] = 1
                continue
            hmap[char] += 1

        for char in t:
            if char not in hmap:
                return False
            hmap[char] -= 1

        for val in hmap.values():
            if val != 0:
                return False

        return True


Solution().isAnagram("anagram", "nagaram")
