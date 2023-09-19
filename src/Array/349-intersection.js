// Given two integer arrays nums1 and nums2, return an array of their intersection.
// Each element in the result must be unique and you may return the result in any order.

// A solução tem complexidade O(n + m) e usa o set.has que é bem mais rápido do que includes. https://stackoverflow.com/questions/55057200/is-the-set-has-method-o1-and-array-indexof-on

var intersection = function (nums1, nums2) {
    const set1 = new Set(nums1)
    const set2 = new Set(nums2)
    const inter = [...set1].filter((element) => set2.has(element))
    return inter
}

console.log(intersection([1, 2, 2, 1], [2, 2]))
console.log(intersection([4, 9, 5], [9, 4, 9, 8, 4]))
