/*class NomeDaClasse {  
   <atributos> 
   <construtor>
   <getters/setters> 
   <métodos> 
}*/

class Pessoa{
  String nome;
  int idade;

  // Maneira clássica parecida com Java;
  /*Pessoa(String nome, int idade){
    this.nome = nome;
    this.idade = idade;
  }*/

  // Novo estilo
  Pessoa(this.nome, this.idade);

  // Construtor nomeado
  Pessoa.simples(this.nome);
  
}

void main(){
  Pessoa p1 = Pessoa("Henrique", 23);
  print(p1.nome);
  print(p1.idade);
  
  Pessoa p2 = Pessoa.simples("Alan");
  print(p2.nome);
  print(p2.idade);

}