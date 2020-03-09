var myImage = document.querySelector('img');

myImage.onclick = function() {
    var mySrc = myImage.getAttribute('src');
    if(mySrc === 'images/firefox.jpg') {
      myImage.setAttribute ('src','images/firefox2.jpeg');
    } 
    if (mySrc === 'images/firefox2.jpeg') {
      myImage.setAttribute ('src','images/firefox.jpg');
    }
}

document.getElementById('data').innerHTML = Date();


var fruits, text, fLen, i;
fruits = ["Banana", "Orange", "Apple", "Mango"];
fLen = fruits.length;

text = "<ul>";
for (i = 0; i < fLen; i++) {
  text += "<li>" + fruits[i] + "</li>";
}
text += "</ul>";
document.getElementById("demo").innerHTML = text;


// ==============================================
/*
 * A variable declared without a value will have the value undefined.
 * var x = 2 + 3 + "5"    Resultado: 55 (string) When adding a number and a string, JavaScript will treat the number as a string.
 * var x = {firstName:"John", lastName:"Doe"};    // Object
 * 
 * ==================================================================
 * The JavaScript this keyword refers to the object it belongs to.
 *  It has different values depending on where it is used:
 * In a method, this refers to the owner object.
 * Alone, this refers to the global object.
 * In a function, this refers to the global object.
 * In a function, in strict mode, this is undefined.
 * In an event, this refers to the element that received the event.
 * Methods like call(), and apply() can refer this to any object.
 *
 * ===========================================================
 * ==	equal to 
 * ===	equal value and equal type
 * 
 * =======================================================
 * JavaScript Data Types
    In JavaScript there are 5 different data types that can contain values:

    string
    number
    boolean
    object
    function
    There are 6 types of objects:

    Object
    Date
    Array
    String
    Number
    Boolean
    And 2 data types that cannot contain values:

    null
    undefined

  * ============================== Expressões Regulares ==========================
  * Use a string to do a search for "W3schools" in a string:
      var str = "Visit W3Schools!";
      var n = str.search("W3Schools");
    Use a regular expression to do a case-insensitive search for "w3schools" in a string:
      var str = "Visit W3Schools";
      var n = str.search(/w3schools/i);
  
  * ============================== ERROS ======================================
    try {
      adddlert("Welcome guest!");
    }
    catch(err) {
      document.getElementById("demo").innerHTML = err.message;
    }
 *
 
 * =================================== Váriaveis ================================
 JavaScript Declarations are Hoisted
  In JavaScript, a variable can be declared after it has been used.
  In other words; a variable can be used before it has been declared.
  Variables and constants declared with let or const are not hoisted!

  * ====================================== Classes ==============================

  class Car {
    constructor(brand) {
      this.carname = brand;
    }
  }
  mycar = new Car("Ford");
 

*/