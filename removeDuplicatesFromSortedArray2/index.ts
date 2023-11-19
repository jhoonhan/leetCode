function removeDuplicates(nums: number[]): number {
  let k = 0;
  let double = false;
  let prev: number | null = null;
  for (let i = 0; i < nums.length; i++) {
    if (nums[i] !== prev) {
      nums[k] = nums[i];
      k += 1;
      double = false;
    }
    if (nums[i] === prev && !double) {
      nums[k] = nums[i];
      k += 1;
      double = true;
    }
    prev = nums[i];
  }
  console.log(nums);
  return k;
}

removeDuplicates([1, 1, 1, 2, 2, 3]);
