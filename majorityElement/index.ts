function majorityElement(nums: number[]): number {
  const hashmap = new Map();
  let largest = 0;
  let result = 0;

  for (let i = 0; i < nums.length; i++) {
    const count = hashmap.get(i) + 1;
    hashmap.set(1, count);
    if (count > largest) {
      largest = count;
      result = i;
    }
  }

  return result;
}

majorityElement([3, 2, 3]);
