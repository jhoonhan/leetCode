///////////// 203ms
function twoSum(nums: number[], target: number): number[] {
  // let num1: number = -1;
  // let num2: number = -1;

  // nums.forEach((el, i1, arr) => {
  //   arr.forEach((el2, i2) => {
  //     if (i1 !== i2 && el + el2 === target) {
  //       num1 = i1;
  //       num2 = i2;
  //     }
  //   });
  // });

  // const result = [num1, num2];
  // return result;

  // Time complexity = O(n^2)
  // Space complexity = O(1)
  // for (let i = 0; i < nums.length; i++) {
  //   for (let j = i + 1; j < nums.length; j++) {
  //     if (nums[i] + nums[j] === target) return [i, j];
  //   }
  // }

  // Hashmap
  // Better Time complexity
  /*
  map = {1:0, 7:1, 5: 2,   }
  [1,2,5,9]
  i = 3
  value = 9
  comple = 10 - 9 = 1
  */

  const map: Map<number, number> = new Map();
  for (let i = 0; i < nums.length; i++) {
    let value = nums[i];
    let complementPair = target - value;
    if (map.has(complementPair)) {
      return [map.get(complementPair), i];
    }
    map.set(value, i);
  }

  // Never will hit here
  return [-1, -1];
}
