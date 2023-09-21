// Given an array nums of size n, return the majority element.
// The majority element is the element that appears more than ⌊n / 2⌋ times. You may assume that the majority element always exists in the array.

/**
 * @param {number[]} nums
 * @return {number}
 */

// É possível encontrar o elemento majoritário com uma complexidade de espaço O(1) usando o algoritmo "Boyer-Moore Voting Algorithm".
// A ideia principal do algoritmo é que, se contarmos um candidato à maioria como +1 e qualquer outro número como -1, então, somando tudo,
//  o elemento majoritário certamente estará acima de 0.

// The Boyer-Moore voting algorithm is one of the popular optimal algorithms which is used to find the majority element among the
// given elements that have more than N/ 2 occurrences. This works perfectly fine for finding the majority element which takes 2
//  traversals over the given elements, which works in O(N) time complexity and O(1) space complexity.

var majorityElement = function (nums) {
    let count = 0
    let candidate = null

    for (let num of nums) {
        if (count === 0) {
            candidate = num
        }
        count += num === candidate ? 1 : -1
    }

    return candidate
}

console.log(majorityElement([3, 2, 3])) // Expected output: 3
console.log(majorityElement([2, 2, 1, 1, 1, 2, 2])) // Expected output: 2
