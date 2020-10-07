//var input = require('fs').readFileSync('/dev/stdin', 'utf8');
var input = require("fs").readFileSync("stdin", "utf8");
var lines = input.split("\n");

testeCases = Number(lines[0]);

function caeser(chave, string) {
  var resultado = "";
  for (var i = 0; i < string.length; i++) {
    var code = string.charCodeAt(i);
    if (code >= 65 && code <= 90) {
      code -= 65;
      code = (code - chave + 26) % 26;
      code += 65;
    }
    resultado += String.fromCharCode(code);
  }
  console.log(resultado);
}

for (let i = 1, j = 2; j <= testeCases * 2; i += 2, j += 2) {
  const string = lines[i];
  const chave = lines[j];
  caeser(chave, string);
}
