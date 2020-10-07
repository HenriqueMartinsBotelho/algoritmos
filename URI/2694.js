//var input = require('fs').readFileSync('/dev/stdin', 'utf8');
var input = require("fs").readFileSync("stdin", "utf8");
var lines = input.split("\n");

testeCases = Number(lines[0]);

function extraiNumeros(s) {
  let x = s.match(/\d+/g);
  let numeros = x.map(e => Number(e));
  let soma = 0;
  for (let index = 0; index < numeros.length; index++) {
    const element = numeros[index];
    soma += element;
  }
  console.log(soma);
}

let string = "";
for (i = 1; i <= testeCases; i++) {
  string = lines[i];
  extraiNumeros(string);
}
