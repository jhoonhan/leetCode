class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        hashmap = {}
        for char in magazine:
            if char not in hashmap:
                hashmap[char] = 1
            else:
                hashmap[char] += 1

        for char in ransomNote:
            if char not in hashmap or hashmap[char] <= 0:
                return False
            else:
                hashmap[char] -= 1
        return True


Solution().canConstruct("aa", "ab")
