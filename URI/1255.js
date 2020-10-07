//var input = require('fs').readFileSync('/dev/stdin', 'utf8');
var input = require("fs").readFileSync("stdin", "utf8");
var lines = input.split("\n");

testeCases = Number(lines[0]);

function removeStrange(string) {
  string = string.toLowerCase();
  let x = string.match(/[a-z]/gi);
  x = x.join("");
  return x;
}

function maiores(objeto) {
  let letras = "";
  let maior = -1;
  for (var o in objeto) {
    if (objeto[o] > maior) {
      maior = objeto[o];
    }
  }
  for (var x in objeto) {
    if (objeto[x] === maior) {
      letras = letras + x;
    }
  }
  console.log(letras);
}

function conta(string) {
  let objeto = {};
  string = removeStrange(string);
  for (let s = 0; s < string.length; s++) {
    const letra = string[s];
    if (objeto[letra]) {
      objeto[letra] += 1;
    } else {
      objeto[letra] = 1;
    }
  }
  maiores(objeto);
}

let string = "";
for (i = 1; i <= testeCases; i++) {
  conta(lines[i]);
}
