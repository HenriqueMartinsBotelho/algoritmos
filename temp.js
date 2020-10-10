var twoSum = function (nums, target) {
  for (let i = 0; i < nums.length; i++) {
    for (let j = 0; j < nums.length; j++) {
      if (nums[i] + nums[j] === target) {
        if (i !== j) {
          return [i, j];
        }
      }
    }
  }
};

let nums = [10, 20, 30, 40, 50, 60];
let target = 70;

console.log(twoSum(nums, target));
