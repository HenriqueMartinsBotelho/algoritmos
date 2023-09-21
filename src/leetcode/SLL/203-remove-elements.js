// Given the head of a linked list and an integer val, remove all the nodes of the
//  linked list that has Node.val == val, and return the new head.

// https://leetcode.com/submissions/detail/1054055587/

/**
 * Definition for singly-linked list.
 * function ListNode(val, next) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.next = (next===undefined ? null : next)
 * }
 */
/**
 * @param {ListNode} head
 * @param {number} val
 * @return {ListNode}
 */

var removeElements = function (head, val) {
    while (head !== null && head.val === val) {
        head = head.next
    }

    if (head === null) return null

    let current = head
    while (current.next !== null) {
        if (current.next.val === val) {
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

let head1 = arrayToList([1, 2, 6, 3, 4, 5, 6])
let result1 = removeElements(head1, 6)
console.log(listToArray(result1)) // Should print [1, 2, 3, 4, 5]
