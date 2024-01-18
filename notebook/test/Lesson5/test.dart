import 'package:collection/collection.dart';

void main(){
  var myList1 = [1, 2, 3];
  var myList2 = ['a', 'b', 'c'];
  var myList3 = [true, false, true];

  var zipped = IterableZip([myList1, myList2, myList3]);

  for (var pair in zipped) {
    print(pair);
  }  
}