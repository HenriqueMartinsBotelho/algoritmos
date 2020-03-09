/*
Imagine you have a shopping cart class that keeps a private List<double> of prices. Add the following:

A getter called total that returns the sum of the prices
A setter that replaces the list with a new one, as long as the new list doesn’t
contain any negative prices (in which case the setter should throw an InvalidPriceException).
 */

class InvalidPriceException {}

class ShoppingCart {
  List<double> _prices = [];
  
  double get total => _prices.fold(0, (e, t) => e + t);
  
  set prices(List<double> value) {
    if (value.any((p) => p < 0)) {
      throw InvalidPriceException();
    }
    
    _prices = value;
  }
}