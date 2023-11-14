function lengthOfLongestSubstring(s: string): number {
  let str = "";
  let previousCount: number = 0;
  let longestCount: number = 0;

  for (let i = 0; i < s.length; i++) {
    if (!str.includes(s[i])) {
      str += s[i];
      previousCount += 1;
    } else {
      if (previousCount > longestCount) {
        longestCount = previousCount;
      }

      const charIndex = str.indexOf(s[i]);
      str = str.slice(charIndex + 1) + s[i];
      console.log(str);
      previousCount = str.length;
    }
  }

  const result = Math.max(longestCount, previousCount);
  console.log(result);

  return result;
}

lengthOfLongestSubstring(" ");
// const aang = "01234566789";
// console.log(aang.slice(1));
