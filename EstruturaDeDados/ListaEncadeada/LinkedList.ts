export class LinkedList<T>{
  
  head: Node<T>;
  tail: Node<T>;
  length: number;

  /**
   * cria um novo no é atribui ele a head se data não é null
   */
  constructor(data: T = null) {
    if (data) {
      const headNode = new Node(data);
      this.head = headNode;
      this.tail = headNode;
      this.length = 1;
    } else {
      this.head = null;
      this.tail = null;
      this.length = 0;
    }
  }

  /**
   * returna true se o comprimento da lista é 0
   */
  isEmpty(): boolean {
    return this.length === 0;
  }

  /**
   * Adiciona node no fim da lista
   */
  private linkLast(e: T){
    let newNode = new Node(e);
    if (this.isEmpty()) {
      this.head = this.tail = newNode;
    } else {
      this.tail.next = newNode;
      this.tail = newNode;
    }
    this.length++;
  }

  /**
   * Insere elemento no fim da lista
   */
  add(e: T): boolean {
    this.linkLast(e);
    return true;
  }

  /**
   * adiciona no no inicio da lista
   */
  addFirst(e: T) {
    if (this.isEmpty()) {
      this.head = this.tail = new Node(e);
    } else {
      let tempNode = this.head;
      this.head = new Node(e);
      this.head.next = tempNode;
    }
    this.length++;
  }

  /**
   * add the node in the last of the linkedList
   * @param e
   */
  addLast(e: T) {
    this.linkLast(e);
  }

  /**
   * add a node at provided index with data
   * @param data
   * @param index
   */
  addAt(data: T, index: number) {
    if (index < 0 || index > this.length) throw new Error("Illegal argument");
    if (index === 0) this.addFirst(data);
    else if (index === this.length) this.linkLast(data);
    else {
      let currentNode = this.head;
      for (let i = 0; i < index - 1; i++) {
        currentNode = currentNode.next;
      }
      const newNode = new Node(data);
      const tempNode = currentNode.next;
      currentNode.next = newNode;
      newNode.next = tempNode;
      this.length++;
    }
  }

  private addFrom(startNode: Node<T>, l: Array<T>): void{
    if(!l) throw new Error('NullPointerException');
    if(!startNode){
      for(let content of l){
        this.linkLast(content);
      }
    }else{
      for(let content of l){
        const newNode = new Node<T>(content);
        let tempNode = startNode.next;
        startNode.next = newNode;
        newNode.next = tempNode;
        startNode = newNode;
        this.length++;
      }
    }
  }
}

class Node<T> {
  data: T;
  next: Node<T>;

  constructor(data: T) {
    this.data = data;
    this.next = null;
  }
}