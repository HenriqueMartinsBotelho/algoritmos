// Given two strings needle and haystack, return the index of
// the first occurrence of needle in haystack, or -1
// if needle is not part of haystack.

// Esse é um problema clássico de encontrar uma substring em uma string maior

// https://leetcode.com/submissions/detail/1051349121/

/**
 * @param {string} haystack
 * @param {string} needle
 * @return {number}
 */

var strStr = function (haystack, needle) {
    if (needle === '') return 0
    if (needle.length > haystack.length) return -1

    for (let i = 0; i <= haystack.length - needle.length; i++) {
        let found = true
        for (let j = 0; j < needle.length; j++) {
            if (haystack[i + j] !== needle[j]) {
                found = false
                break
            }
        }
        if (found) return i
    }

    return -1
}

console.log(strStr('sadbutsad', 'sad'))
console.log(strStr('sadbutsad', 'dad'))

// Solução alternativa:

// var strStr = function(haystack, needle) {
//     return haystack.indexOf(needle)
// };
