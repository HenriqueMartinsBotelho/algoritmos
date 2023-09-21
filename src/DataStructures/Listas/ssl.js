function ListNode(val, next) {
    this.val = val === undefined ? 0 : val
    this.next = next === undefined ? null : next
}

let node3 = new ListNode(3)
let node2 = new ListNode(2, node3)
let head = new ListNode(1, node2)

function printList(node) {
    while (node !== null) {
        console.log(node.val)
        node = node.next
    }
}

printList(head)
