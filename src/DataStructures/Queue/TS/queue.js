var Queue = /** @class */ (function () {
    function Queue() {
        this.items = [];
    }
    Queue.prototype.push = function (item) {
        this.items.push(item);
    };
    Queue.prototype.pop = function () {
        this.items.shift();
    };
    Queue.prototype.front = function () {
        return this.items[0];
    };
    Queue.prototype.isEmpty = function () {
        return this.items.length === 0;
    };
    Queue.prototype.size = function () {
        return this.items.length;
    };
    Queue.prototype.print = function () {
        console.log(this.items.toString());
    };
    return Queue;
}());
// Testing Queue
var queue = new Queue();
queue.push("Banana");
queue.push("Abacate");
queue.push("Queijo");
queue.front();
queue.pop();
queue.print();
