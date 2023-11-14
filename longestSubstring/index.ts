function lengthOfLongestSubstring(s: string): number {
  let str = "";
  let longestCount: number = 0;

  for (let i = 0; i < s.length; i++) {
    if (!str.includes(s[i])) {
      str += s[i];
    } else {
      if (str.length > longestCount) {
        longestCount = str.length;
      }
      str = s[i];
    }
  }
  return longestCount;
}

lengthOfLongestSubstring("pwwkew");
