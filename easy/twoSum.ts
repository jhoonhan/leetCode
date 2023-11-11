function twoSum(nums: number[], target: number): number[] {
  let num1: number = -1;
  let num2: number = -1;

  nums.forEach((el, i1, arr) => {
    arr.forEach((el2, i2) => {
      if (i1 !== i2 && el + el2 === target) {
        num1 = i1;
        num2 = i2;
      }
    });
  });

  const result = [num1, num2];
  return result;
}
