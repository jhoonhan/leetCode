/**
 Do not return anything, modify nums1 in-place instead.
 */

function merge(nums1: number[], m: number, nums2: number[], n: number): void {
  let last = m + n - 1;

  // last = 8, m = 6, n = 3
  while (m > 0 && n > 0) {
    if (nums1[m - 1] > nums2[n - 1]) {
      nums1[last] = nums1[m - 1];
      m -= 1;
    } else {
      nums1[last] = nums2[n - 1];
      n -= 1;
    }
    last -= 1;
  }

  // Fill nums1 with leftoveer in nums2
  while (n > 0) {
    nums1[last] = nums2[n - 1];
    n -= 1;
    last -= 1;
  }
}

merge([1, 2, 3, 4, 5, 6, 0, 0, 0], 6, [20, 50, 60], 3);
