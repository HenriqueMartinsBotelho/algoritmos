interface ExQueue<T> {
    push(item: T): void // Add item to the end of queue
    pop(): void // Remove item from the end of queue
    front(): T | undefined // Returns first element of queue
    isEmpty(): boolean // Verify if queue is empty
    size(): number // Returns number of elements
    print(): void // Print queue
}

class ExQueue<T> implements ExQueue<T> {
    items: T[] = []

    push(item: T): void {
        this.items.push(item)
    }

    pop(): void {
        this.items.shift()
    }

    front(): T {
        return this.items[0]
    }

    isEmpty(): boolean {
        return this.items.length === 0
    }

    size(): number {
        return this.items.length
    }

    print(): void {
        console.log(this.items.toString())
    }
}

// Testing ExQueue

const exqueue = new ExQueue<string>()
exqueue.push('Banana')
exqueue.push('Abacate')
exqueue.push('Queijo')
exqueue.front()
exqueue.pop()
exqueue.print()
