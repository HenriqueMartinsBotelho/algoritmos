// Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.

// Note that you must do this in-place without making a copy of the array.

/**
 * @param {number[]} nums
 * @return {void} Do not return anything, modify nums in-place instead.
 */
var moveZeroes = function (nums) {
    var index = 0
    for (var i = 0; i < nums.length; i++) {
        var n = nums[i]
        if (n !== 0) {
            nums[index++] = n
        }
    }

    for (index; index < nums.length; index++) {
        nums[index] = 0
    }
}

// Solução 2
// var moveZeroes = function (nums) {
//     let lastIndex = 0
//     for (let index = 0; index < nums.length; index++) {
//         if (nums[index] !== 0) {
//             nums[lastIndex] = nums[index]
//             if (index !== lastIndex) {
//                 nums[index] = 0
//             }
//             lastIndex++
//         }
//     }
//     return nums
// }

console.log(moveZeroes([0, 1, 0, 3, 12])) // Expected: [1,3,12,0,0]

console.log(moveZeroes([0])) // Expected: [0]
