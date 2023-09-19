type element = {
    priority: number
    index: number
}

interface Heap<element> {
    addElement(e: element): void
    print(): void
    correct_going_down(e: element): void
}

class Heap<element> implements Heap<element> {
    elements: element[] = []

    addElement = (e: element) => {
        this.elements.push(e)
    }

    correct_going_down = (ne: element) => {
        for (const e of this.elements) {
            let i = e['index']
            let maior = i
            if (2 * i <= this.elements.length) {
                console.log('continuar algoritmo')
            }
            if (maior !== i) {
                console.log('não usar curso da carla muito confuso')
                console.log(
                    'https://www.google.com/search?q=correct+heap+going+down+pseudocode'
                )
            }
        }
    }

    print = () => {
        console.log(this.elements)
    }
}

const e0: element = {
    priority: 30,
    index: 0,
}

const e1: element = {
    priority: 27,
    index: 1,
}

const e2: element = {
    priority: 24,
    index: 2,
}

const e3: element = {
    priority: 20,
    index: 3,
}

const e4: element = {
    priority: 25,
    index: 4,
}

const e5: element = {
    priority: 19,
    index: 5,
}

const e6: element = {
    priority: 22,
    index: 6,
}

const e7: element = {
    priority: 11,
    index: 7,
}

const e8: element = {
    priority: 15,
    index: 8,
}

const e9: element = {
    priority: 23,
    index: 9,
}

const e10: element = {
    priority: 18,
    index: 10,
}

const e11: element = {
    priority: 14,
    index: 11,
}

const e12: element = {
    priority: 10,
    index: 12,
}

const e13: element = {
    priority: 17,
    index: 13,
}

const e14: element = {
    priority: 21,
    index: 14,
}

const e15: element = {
    priority: 8,
    index: 15,
}

const e16: element = {
    priority: 1,
    index: 16,
}

const e17: element = {
    priority: 3,
    index: 17,
}

const e18: element = {
    priority: 4,
    index: 18,
}

const e19: element = {
    priority: 9,
    index: 19,
}

const e20: element = {
    priority: 7,
    index: 20,
}

const e21: element = {
    priority: 6,
    index: 21,
}

const heap = new Heap<element>()
heap.addElement(e0)
heap.addElement(e1)
heap.addElement(e3)
heap.addElement(e3)
heap.addElement(e4)
heap.addElement(e5)
heap.addElement(e6)
heap.addElement(e7)
heap.addElement(e8)
heap.addElement(e9)
heap.addElement(e10)
heap.addElement(e11)
heap.addElement(e12)
heap.addElement(e13)
heap.addElement(e14)
heap.addElement(e15)
heap.addElement(e16)
heap.addElement(e17)
heap.addElement(e18)
heap.addElement(e19)
heap.addElement(e20)
heap.addElement(e21)
heap.correct_going_down(e1)
heap.print()
