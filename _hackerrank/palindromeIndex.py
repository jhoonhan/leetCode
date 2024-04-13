def palindromeIndex(s):

    def isPalindrome(s):
        half = len(s) // 2
        return s[:half] == s[half + len(s) % 2 :][::-1]

    left, right = 0, len(s) - 1

    while left < right:
        if s[left] != s[right]:
            return left if isPalindrome(s[:left] + s[left + 1 :]) else right
        left += 1
        right -= 1

    return -1


palindromeIndex("aabbccaa")
