function lengthOfLongestSubstring(s: string): number {
    let str = "";
    let longestCount = 0;

    // O(n)
    for (let i = 0; i < s.length; i++) {
        if (!str.includes(s[i])) {
            str += s[i];
            // console.log(str);
        } else {
            if (str.length > longestCount) {
                longestCount = str.length;
            }
            str = str.slice(str.indexOf(s[i]) + 1) + s[i];
            console.log(str);
        }
    }

    return Math.max(longestCount, str.length);
}

lengthOfLongestSubstring("aabaab!bb");
// const aang = "01234566789";
// console.log(aang.slice(1));
