//var input = require('fs').readFileSync('/dev/stdin', 'utf8');
var input = require("fs").readFileSync("stdin", "utf8");
var lines = input.split("\n");

espacamento = parseInt(lines[0]);

function retornaMinutos(espacamento) {
  let naochegou = true;
  let minutos = 1;
  let car1dist;
  let car2dist;
  while (naochegou) {
    car1dist = 60 * (minutos / 60);
    car2dist = 90 * (minutos / 60);
    if (car2dist - car1dist >= espacamento) {
      naochegou = false;
    }
    minutos++;
  }
  return minutos - 1;
}

console.log(retornaMinutos(espacamento) + " minutos"); // 60
