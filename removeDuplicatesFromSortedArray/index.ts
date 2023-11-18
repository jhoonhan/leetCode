function removeDuplicates(nums: number[]): number {
  let k = 0;
  let prev: number | null = null;
  for (let i = 0; i < nums.length; i++) {
    if (nums[i] !== prev) {
      nums[k] = nums[i];
      k += 1;
    }
    prev = nums[i];
  }
  return k;
}

removeDuplicates([1, 1, 2]);
