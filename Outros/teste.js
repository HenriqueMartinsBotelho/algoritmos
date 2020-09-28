let vetor = [
  { name: "Alice", age: 10 },
  { name: "Bob", age: 20 },
];

function pessoas(array) {
  let nomes = [];
  let idades = [];
  array.forEach(function imprime(element) {
    nomes.push(element.name);
    idades.push(element.age);
  });

  let objeto = { nomes: nomes, idades: idades };

  return objeto;
}

console.log(pessoas(vetor));
