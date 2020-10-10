const Stack = function () {
  let items = [];

  //Adiciona um novo item à pilha. Theta(1)
  this.push = (element) => {
    items.push(element);
  };

  // Remove o item do topo da pilha
  this.pop = function () {
    return items.pop();
  };

  //devolve o elemento que está no topo da pilha
  this.peek = function () {
    return items[items.length - 1];
  };

  //informa se a pilha esta vazia ou não
  this.isEmpty = function () {
    return items.length === 0;
  };

  //limpa a pilha
  this.clear = function () {
    items = [];
  };

  //retorna o tamanho da pilha
  this.size = function () {
    return items.length;
  };

  //imprime a pilha
  this.print = function () {
    console.log(items.toString());
  };
};

// Testando Pilha
let stack = new Stack();
stack.push(10);
stack.push(20);
console.log(stack.peek());
stack.print();

export default Stack;
