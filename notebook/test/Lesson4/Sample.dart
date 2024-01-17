import 'dart:core';

void main() {
  int a=3,b=2;
  if (a>b && b==1){
    print("a>b");
  } else {
    print("a<=b");
  }

  print("\nSample4");
  List l = List.generate(12, (index) => index);
  for (var i in l) {
    print((i+1).toString()+"月のデータです。");
  }

  print("\nSample6");
  List l1 = List.generate(5, (index) => index);
  List l2 = List.generate(3, (index) => index);
  for (var i in l1) {
    for (var j in l2) {
      print("iは"+(i).toString()+":jは"+(j).toString());
    }
  }

}
