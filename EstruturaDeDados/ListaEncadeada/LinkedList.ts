class LinkedList{
    public start: LinkedListNode | null = null

    //Complexity: 
    public addToTail(value: any): void{
        const newNode = new LinkedListNode()
        newNode.value = value
        let node = this.start
        while(node !== null){
            node = node.next
        }
    }
}

class LinkedListNode{
    public value: any
    public next: LinkedListNode | null
}


// Criação dos nós
const firstNode = new LinkedListNode()
firstNode.value = 5
const secondNode = new LinkedListNode()
secondNode.value = 13

// Inicialização da Lista
const list = new LinkedList()
list.start = firstNode
firstNode.next = secondNode;

console.log(list)