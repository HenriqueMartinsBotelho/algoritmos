import 'superclasse.dart';

class Filho extends Pai{
  
  int metodo3(){
    return 3;
  }

}

void main(){

  Filho f = new Filho();
  print(f.publico);
  print(f.privado);
  print(f.metodo1()); 
  print(f.metodo2());
  print(f.metodo3());

}



