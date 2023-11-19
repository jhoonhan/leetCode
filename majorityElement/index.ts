function majorityElement(nums: number[]): number {
  const hashmap = new Map();
  let largest = 0;
  let result = 0;

  for (let i = 0; i < nums.length; i++) {
    const mapCount = hashmap.get(nums[i]) + 1;
    const count = Number.isNaN(mapCount) ? 1 : mapCount;
    hashmap.set(nums[i], count);
    if (count > largest) {
      largest = count;
      result = nums[i];
    }
  }
  return result;
}

majorityElement([1]);
