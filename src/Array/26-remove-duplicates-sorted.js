// Given an integer array nums sorted in non-decreasing order, remove the duplicates in-place such that each unique element appears only once.
// The relative order of the elements should be kept the same. Then return the number of unique elements in nums.

// https://leetcode.com/submissions/detail/1048716334/

/**
 * @param {number[]} nums
 * @return {number}
 */

var removeDuplicates = function (nums) {
    let p = 0
    for (let index = 0; index < nums.length; index++) {
        const element = nums[index]
        if (nums[index] !== nums[index + 1]) {
            nums[p] = element
            p++
        }
    }
    return p
}

removeDuplicates([1, 1, 2]) //  [1,2,_]
removeDuplicates([0, 0, 1, 1, 1, 2, 2, 3, 3, 4]) // [0,1,2,3,4,_,_,_,_,_]

// Outra solução

/**
 * @param {number[]} nums
 * @return {number}
 */

// Abordagem:
// Podemos usar dois ponteiros i e j, onde i aponta para o último elemento único encontrado até agora e j aponta para o elemento atual que está sendo examinado.
// Se nums[i] e nums[j] forem iguais, apenas incrementamos j.
//  Caso contrário, incrementamos i e copiamos nums[j] para nums[i]. No final, retornamos i+1, que representa o comprimento do array modificado.

// var removeDuplicates = function(nums) {
//     let i = 0;
//     for (let j = 1; j < nums.length; j++) {
//       if (nums[i] !== nums[j]) {
//         i++;
//         nums[i] = nums[j];
//       }
//     }
//     return i + 1;
//   }
