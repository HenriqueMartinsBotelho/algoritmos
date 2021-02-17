function LinkedList() {
  let Node = function (element) {
    this.element = element;
    this.next = null;
  };

  let length = 0;
  let head = null;

  // Add an element to the end of the list
  this.append = function (element) {
    let node = new Node(element);
    let current;
    if (head === null) {
      head = node;
    } else {
      current = head;
      while (current.next) {
        current = current.next;
      }
      current.next = node;
    }
    length++;
  };
  // Add an element at a specific position
  this.insert = function (position, element) {};

  // Revemo an element at a specific position
  this.removeAt = function (position) {};
  // Remove the element element
  this.remove = function (element) {};

  // Retorn the element position
  this.indexOf = function (element) {};

  // Verify if the list is empty
  this.isEmpty = function () {};

  // Retorn the size of the list
  this.size = function () {};

  // Convert in string
  this.toString = function () {
    let current = head;
    let string = "";
    while (current) {
      string += current.element + "";
      current = current.next;
    }
    return string;
  };
  // Print list in console
  this.print = function () {
    console.log(this.toString());
  };
}

let list = new LinkedList();
list.append("Henrique");
list.append("Martins");
list.append("Botelho");
