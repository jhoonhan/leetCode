class Solution:
    def groupAnagrams(self, strs: list) -> list[list]:
        res = defaultdict(list)
        for chars in strs:
            count = [0] * 26
            for char in chars:
                count[ord(char) - ord("a")] += 1
            res[tuple(count)].append(chars)
        return res.values()


Solution().groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"])
