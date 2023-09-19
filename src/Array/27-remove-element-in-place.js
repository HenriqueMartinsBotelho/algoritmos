// Given an integer array nums and an integer val, remove all occurrences of val in nums in-place.
// The order of the elements may be changed. Then return the number of elements in nums which are not equal to val.

/**
 * @param {number[]} nums
 * @param {number} val
 * @return {number}
 */

var removeElement = function (nums, val) {
    let p = 0
    for (let index = 0; index < nums.length; index++) {
        const element = nums[index]
        if (element !== val) {
            nums[p] = element
            p++
        }
    }
    return p
}

console.log(removeElement([3, 2, 2, 3], 3)) // 2,  [2,2,_,_]
console.log(removeElement([0, 1, 2, 2, 3, 0, 4, 2], 2)) //5,  [0,1,4,0,3,_,_,_]
