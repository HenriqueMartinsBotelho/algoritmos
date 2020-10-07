//var input = require('fs').readFileSync('/dev/stdin', 'utf8');
var input = require("fs").readFileSync("stdin", "utf8");
var lines = input.split("\n");

testeCases = Number(lines[0]);

function junta(s, s1) {
  let s3 = "";
  let resto = "";
  if (s.length <= s1.length) {
    for (let index = 0; index < s.length; index++) {
      s3 = s3 + s[index] + s1[index];
    }
    resto = s1.slice(s.length, s1.length);
    s3 += resto;
  } else {
    for (let index = 0; index < s1.length; index++) {
      s3 = s3 + s1[index] + s[index];
    }
    resto = s.slice(s1.length, s.length);
    s3 += resto;
  }
  return s3;
}

for (let index = 1; index <= testeCases; index++) {
  const string = lines[index];
  palavras = string.split(" ");
  newString = junta(palavras[0], palavras[1]);
  console.log(newString);
}
