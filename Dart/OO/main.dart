/*class NomeDaClasse {  
   <atributos> 
   <métodos> 
}*/
 
class Car {  
   // atributos 
   String engine = "E1001";  
   
   // métodos
   void disp() { 
      print(engine); 
   } 
}

void main() { 
   Car c= new Car(); 
   c.disp(); 
} 