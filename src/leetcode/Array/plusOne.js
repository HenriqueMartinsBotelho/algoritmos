// 66 - https://leetcode.com/problems/plus-one/
// You are given a large integer represented as an integer array digits, where each digits[i] is the ith digit of the integer. The digits are ordered from most significant to least significant in left-to-right order. The large integer does not contain any leading 0's.

// Increment the large integer by one and return the resulting array of digits.

/**
 * @param {number[]} digits
 * @return {number[]}
 */
var plusOne = function (digits) {
    for (let i = digits.length - 1; i >= 0; i--) {
        digits[i]++

        if (digits[i] > 9) {
            digits[i] = 0
        } else {
            return digits
        }
    }

    digits.unshift(1)
    return digits
}

console.log(plusOne([9]))
console.log(plusOne([1, 2, 3]))
console.log(plusOne([9, 9, 9]))
console.log(plusOne([8, 9, 9, 9]))
