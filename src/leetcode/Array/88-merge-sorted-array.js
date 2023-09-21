// You are given two integer arrays nums1 and nums2, sorted in non-decreasing order, and two integers m and n, representing the number of elements in nums1 and nums2 respectively.

// Merge nums1 and nums2 into a single array sorted in non-decreasing order.

// The final sorted array should not be returned by the function, but instead be stored inside the array nums1. To accommodate this, nums1 has a length of m + n, where the first m elements denote the elements that should be merged, and the last n elements are set to 0 and should be ignored. nums2 has a length of n.

/**
 * @param {number[]} nums1
 * @param {number} m
 * @param {number[]} nums2
 * @param {number} n
 * @return {void} Do not return anything, modify nums1 in-place instead.
 */

// https://leetcode.com/submissions/detail/1048732598/

var merge = function (nums1, m, nums2, n) {
    let p1 = m - 1,
        p2 = n - 1
    let p = m + n - 1

    while (p1 >= 0 && p2 >= 0) {
        if (nums1[p1] > nums2[p2]) {
            nums1[p] = nums1[p1]
            p1--
        } else {
            nums1[p] = nums2[p2]
            p2--
        }
        p--
    }

    while (p2 >= 0) {
        nums1[p] = nums2[p2]
        p2--
        p--
    }
}

merge([1, 2, 3, 0, 0, 0], 3, [2, 5, 6])
merge([1], 11, [])

// Outra solução:

// Essa solução chama sort eu um exercício sobre ordenação e por isso não gosto dela.

// var merge = function(nums1, m, nums2, n) {
//     for (let i = m, j = 0; j < n; i++, j++) {
//         nums1[i] = nums2[j];
//     }
//     nums1.sort((a, b) => a - b);
// };
