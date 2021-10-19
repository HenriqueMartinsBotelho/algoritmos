interface Queue<T> {
    push(item: T): void
    pop(): void
    print(): void
}

class Queue<T> implements Queue<T> {
    items: T[] = []

    push(item: T): void {
        this.items.push(item)
    }

    pop(): void {
        this.items.shift()
    }

    print(): void {
        console.log(this.items.toString())
    }
}

// Testing Queue
const queue = new Queue<string>()
queue.print()
queue.push('Inscreva-se')
queue.print()
queue.push('no meu')
queue.print()
queue.push('canal')
queue.print()
queue.pop()
queue.print()
