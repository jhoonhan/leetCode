function findMedianSortedArrays(nums1: number[], nums2: number[]): number {
  const combinedArr = nums1.concat(nums2);
  const arrLength: number = combinedArr.length;
  const middle: number = arrLength / 2;

  return Number(combinedArr[middle].toFixed(5));
}
