function deleta(vetor, num) {
  for (let index = 0; index < vetor.length; index++) {
    const element = vetor[index];
    if (element === num) {
      vetor.splice(index, 1);
    }
  }
}

function deletaUltimo(vetor) {
  vetor.splice(vetor.length - 1, 1)
}

function deletaPrimeiro(vetor) {
  vetor.splice(0, 1)
}

let v = [10, 20, 30, 40, 50, 60, 70]
// deleta(v, 70)

deletaPrimeiro(v)
console.log(v)


//4  Faria uma cópia do vetor e não copiaria o elemento que quero deletar