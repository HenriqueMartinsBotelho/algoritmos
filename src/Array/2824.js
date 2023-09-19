// Given a 0-indexed integer array nums of length n and an integer target, return the number of pairs (i, j) where 0 <= i < j < n
// and nums[i] + nums[j] < target.

/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number}
 */

// https://leetcode.com/submissions/detail/1050126005/

var countPairs = function (nums, target) {
    let count = 0
    for (let i = 0; i < nums.length; i++) {
        for (let j = i + 1; j < nums.length; j++) {
            if (nums[i] + nums[j] < target) {
                count++
            }
        }
    }
    return count
}

console.log(countPairs([-6, 2, 5, -2, -7, -1, 3], -2))
