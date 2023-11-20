/**
 Do not return anything, modify nums in-place instead.
 */
function rotate(nums: number[], k: number): void {
  7 / 3;
  7 / 2;
  for (let i = k; i > 0; i--) {
    nums.unshift(nums[nums.length - 1]);
    nums.pop();
  }
}

rotate([1, 2, 3, 4, 5, 6, 7], 1);
