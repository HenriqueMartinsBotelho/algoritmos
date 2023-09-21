/**
 * @param {string} s
 * @param {string} t
 * @return {boolean}
 */

// Given two strings s and t, return true if t is an anagram of s, and false otherwise.

// An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

// https://leetcode.com/submissions/detail/1050097490/

var isAnagram = function (s, t) {
    if (s.length !== t.length) return false

    let count = {}

    for (let i = 0; i < s.length; i++) {
        count[s[i]] = (count[s[i]] || 0) + 1
    }

    for (let i = 0; i < t.length; i++) {
        if (!count[t[i]]) return false
        count[t[i]]--
    }

    return true
}

console.log(isAnagram('anagram', 'nagaram')) // true
console.log(isAnagram('car', 'rat')) // false
console.log(isAnagram('aacc', 'ccac')) // false

// Em termos de otimização de espaço, uma abordagem alternativa seria:

// 1. Ordenar ambas as strings s e t.
// 2. Verificar se as strings ordenadas são iguais.

// A complexidade de tempo dessa abordagem seria dominada pelo passo de ordenação, que é O(n log n)
//  para a maioria dos algoritmos de ordenação, e a complexidade de espaço seria
// O(1) se a ordenação for feita in-place (ou seja, sem usar memória adicional).

// A abordagem original com contagem é mais eficiente em termos de tempo (O(n)), mas usa mais espaço (
// O(1) com um limite superior de 26 entradas, no caso das letras do alfabeto inglês).
// A abordagem de ordenação é um pouco menos eficiente em termos de tempo O(nlogn)), mas pode ser mais eficiente em termos de espaço (
// O(1)).
