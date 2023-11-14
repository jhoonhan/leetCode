function lengthOfLongestSubstring(s: string): number {
  let str = "";
  let longestCount = 0;

  // O(n)
  for (let i = 0; i < s.length; i++) {
    if (!str.includes(s[i])) {
      str += s[i];
    } else {
      if (str.length > longestCount) {
        longestCount = str.length;
      }
      str = str.slice(str.indexOf(s[i]) + 1) + s[i];
    }
  }

  const result = Math.max(longestCount, str.length);

  return result;
}

lengthOfLongestSubstring("");
// const aang = "01234566789";
// console.log(aang.slice(1));
