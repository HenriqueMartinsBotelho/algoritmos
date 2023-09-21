var singleNumber = function (nums) {
    let sum = 0
    for (i in nums) {
        sum ^= nums[i]
    }
    return sum
}

console.log(singleNumber([4, 1, 2, 1, 2]))
