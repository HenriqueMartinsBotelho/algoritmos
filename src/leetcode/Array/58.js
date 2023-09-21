// Given a string s consisting of words and spaces, return the length of the last word in the string.

// A word is a maximal substring consisting of non-space characters only.

// https://leetcode.com/submissions/detail/1052135538/

/**
 * @param {string} s
 * @return {number}
 */

var lengthOfLastWord = function (s) {
    let a = s.trim().split(' ')
    return a[a.length - 1].length
}

console.log(lengthOfLastWord('Hello world   '))
console.log(lengthOfLastWord('   Hello world'))
console.log(lengthOfLastWord('Hello world'))
