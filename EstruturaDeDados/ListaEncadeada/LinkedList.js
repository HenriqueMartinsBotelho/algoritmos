var LinkedListNode = /** @class */ (function () {
    function LinkedListNode() {
    }
    return LinkedListNode;
}());
var LinkedList = /** @class */ (function () {
    function LinkedList() {
        this.start = null;
    }
    return LinkedList;
}());
var firstNode = new LinkedListNode();
var secondNode = new LinkedListNode();
firstNode.value = 5;
secondNode.value = 13;
firstNode.next = secondNode;
var list = new LinkedList();
list.start = firstNode;
console.log(list);
