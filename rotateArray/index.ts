/**
 Do not return anything, modify nums in-place instead.
 */
function rotate(nums: number[], k: number): void {
  // Solution 1: This is slow
  // for (let i = k; i > 0; i--) {
  //   nums.unshift(nums[nums.length - 1]);
  //   nums.pop();
  // }
  //
  // Solution 2
  // for (let i = 0; i < nums.length; i++) {}
  //
  // Solution 3: fastest
  k = k % nums.length;

  let l = 0;
  let r = nums.length - 1;
  // reverse full given array
  // from [1,2,3,4,5,6,7] to [7,6,5,4,3,2,1]
  nums = reverseArr(nums, l, r);

  // reverse part from 0 to k - 1;
  // from [7,6,5,4,3,2,1] to [5,6,7,4,3,2,1]
  l = 0;
  r = k - 1;
  nums = reverseArr(nums, l, r);

  // reverse part from k to the end;
  // from [5,6,7,4,3,2,1] to [5,6,7,1,2,3,4]
  l = k;
  r = nums.length - 1;
  nums = reverseArr(nums, l, r);
  console.log(nums);
}

function reverseArr(nums: number[], l: number, r: number): number[] {
  while (l < r) {
    let temp = nums[l];
    nums[l] = nums[r];
    nums[r] = temp;
    l++;
    r--;
  }

  return nums;
}

rotate([1, 2, 3, 4, 5], 7);
