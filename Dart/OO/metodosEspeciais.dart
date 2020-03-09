/*class NomeDaClasse {  
   <atributos> 
   <getters/setters> 
   <métodos> 
}*/


/* 
"
Getters and setters are special methods that provide read and write access to an object’s properties.
Recall that each instance variable has an implicit getter, plus a setter if appropriate.
You can create additional properties by implementing getters and setters, using the get and set keywords"

https://dart.dev/guides/language/language-tour#getters-and-setters


*/

 
class Pessoa {  
   // atributos 
   String nome;  
   double _peso;
   
   // get
  double get peso => _peso;

  // set
  set peso(double peso){
    if (peso < 500.0 && peso > 0.0) {
      _peso = peso;
    }
  }

}

void main() { 
   Pessoa c = new Pessoa(); 
   c.peso = 200.0; // no set usamos = e não ()
   print(c.peso); // acessando o peso pelo get peso.
} 