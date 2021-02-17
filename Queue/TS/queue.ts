interface IQueue<T> {
  push(item: T): void; // Add item to the end of queue
  pop(): void; // Remove item from the end of queue
  front(): T | undefined; // Returns first element of queue
  isEmpty(): boolean; // Verify if queue is empty
  size(): number; // Returns number of elements
  print(): void; // Print queue
}

class Queue<T> implements IQueue<T> {
  items: T[] = [];

  push(item: T): void {
    this.items.push(item);
  }

  pop(): void {
    this.items.shift();
  }

  front(): T {
    return this.items[0];
  }

  isEmpty(): boolean {
    return this.items.length === 0;
  }

  size(): number {
    return this.items.length;
  }

  print(): void {
    console.log(this.items.toString());
  }
}

// Testing Queue

const queue = new Queue<string>();
queue.push("Banana");
queue.push("Abacate");
queue.push("Queijo");
queue.front();
queue.pop();
queue.print();
