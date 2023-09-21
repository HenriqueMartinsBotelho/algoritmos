// 202. Happy Number

var isHappy = function (n) {
    let mem = new Set()
    while (n !== 1) {
        let sum = 0
        while (n > 0) {
            sum += (n % 10) * (n % 10)
            n = Math.floor(n / 10)
        }
        if (!mem.has(sum)) {
            mem.add(sum)
            n = sum
        } else {
            return false
        }
    }
    return true
}

console.log(isHappy(19))
