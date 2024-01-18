import 'dart:core';
import 'package:collection/collection.dart';
import 'package:quiver/iterables.dart';

// import 'dart:math';
// import 'package:quiver/strings.dart';
// import 'package:quiver/collection.dart';

// import 'dart:io';

// List<int> range(int start, int end, [int step = 1]) {
//   return List<int>.generate((end - start) ~/ step + 1, (i) => start + i * step);
// }
void main(){
  print("\nSample1");
  var sale=[80,60,22,50,75];
  print(sale);

  print("\nSample2");
  print(sale[0]);

  print("\nSample3");
  for (var s in sale) {
    print(s);
  }

  print("\nSample4");
  print("3番のデータを変更します。");
  var sss=List.from(sale);
  sss[3]=99;
  print(sss);

  print("\nSample5");
  sss=List.from(sale);
  print(sss);
  sss.add(100);
  print(sss);
  sss.insert(2,25);
  print(sss);

  print("\nSample6");
  sss=List.from(sale);
  print(sss);
  sss.removeAt(0);
  print(sss);
  sss.remove(22);
  print(sss);

  print("\nSample7");
  sss=List.from(sale);
  var sss2=sss;
  print(sss);
  print(sss2);
  sss[0]=10;
  print(sss);
  print(sss2);

  print("\nSample9");
  var sale1=[1,2,3,4,5,6];
  var sale2=[7,8,9,10,11,12];
  var ysale = sale1+sale2;
  print(sale1);
  print(sale2);
  print(ysale);

  print("\nSample10");
  print(ysale);

  sss=ysale.sublist(0,6);
  print(sss);
  sss2=ysale.sublist(6,);
  print(sss2);

  var sss3 = ysale.where((element) => ysale.indexOf(element) % 2 == 0).toList();
  print("一か月おきのデータは" + sss3.toString() + "です。");

  var sss4=ysale.reversed.toList();
  print(sss4);

  var sss5 = List.from(ysale);
  sss5.setRange(0, 6, [0,0,0,0,0,0]);
  print(sss5);

  print("\nSample12");

  var city = ["東京","名古屋","大阪","京都"];
  sale=[80,60,22,50,75];

  print("都市データ名は"+city.toString()+"です。");
  print("売上データは"+sale.toString()+"です。");

  print("データを組み合わせます。");

  for (var d in IterableZip([city,sale])){
    print(d);
  }

  print("データとインデックスを組み合わせます。");

  for (var d in enumerate(city)){
    print(d);
  }

}
