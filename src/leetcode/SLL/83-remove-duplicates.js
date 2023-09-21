// leetcode 83. Remove Duplicates from Sorted List

// https://leetcode.com/submissions/detail/1054031754/

// Given the head of a sorted linked list, delete all duplicates such that each element appears only once. Return the linked list sorted as well.

/**
 * Definition for singly-linked list.
 * function ListNode(val, next) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.next = (next===undefined ? null : next)
 * }
 */
/**
 * @param {ListNode} head
 * @return {ListNode}
 */
var deleteDuplicates = function (head) {
    let current = head

    while (current !== null && current.next !== null) {
        if (current.val === current.next.val) {
            current.next = current.next.next
        } else {
            current = current.next
        }
    }

    return head
}

// Testes

function ListNode(val, next) {
    this.val = val === undefined ? 0 : val
    this.next = next === undefined ? null : next
}

function arrayToList(nums) {
    let dummy = new ListNode()
    let current = dummy
    for (let num of nums) {
        current.next = new ListNode(num)
        current = current.next
    }
    return dummy.next
}

function listToArray(node) {
    let result = []
    while (node) {
        result.push(node.val)
        node = node.next
    }
    return result
}

// Test 1: List without duplicates
let head1 = arrayToList([1, 2, 3, 4, 5])
let result1 = deleteDuplicates(head1)
console.log(listToArray(result1)) // Should print [1, 2, 3, 4, 5]

// Test 2: List with all duplicates
let head2 = arrayToList([2, 2, 2, 2, 2])
let result2 = deleteDuplicates(head2)
console.log(listToArray(result2)) // Should print [2]

// Test 3: List with some duplicates
let head3 = arrayToList([1, 2, 2, 3, 4, 4, 5])
let result3 = deleteDuplicates(head3)
console.log(listToArray(result3)) // Should print [1, 2, 3, 4, 5]

// Test 4: Empty list
let head4 = arrayToList([])
let result4 = deleteDuplicates(head4)
console.log(listToArray(result4)) // Should print []

// Vídeo legal com outra solução: https://www.youtube.com/watch?v=irBmJbVarQg
