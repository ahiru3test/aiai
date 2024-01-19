import 'dart:core';
import 'dart:io';
import 'package:collection/collection.dart';
import 'package:quiver/iterables.dart';

// import 'dart:math';
// import 'package:quiver/strings.dart';
// import 'package:quiver/collection.dart';

// import 'dart:io';

// List<int> range(int start, int end, [int step = 1]) {
//   return List<int>.generate((end - start) ~/ step + 1, (i) => start + i * step);
// }
int sum(List<int> list) {
 return list.reduce((value, element) => value + element);
}

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

  print("\nSample13");
  city=["東京","名古屋","大阪","京都"];
  sale=[80,60,22,50,75];

  print("都市データ名は"+city.toString()+"です。");
  print("売上データは"+sale.toString()+"です。");

  print("データを組み合わせます。");

  for (var d in IterableZip([city,sale])){
    print(d);
  }

  print("データを分解します。");

  for (var pair in IterableZip([city,sale])){
    print("都市名は"+pair[0].toString()+"売上は"+pair[1].toString());
  }

  print("\nSample14");
  var data=[1,2,3,4,5];
  print("現在のデータは"+data.toString()+"です。");

  // ndata=[n*2 for n in data if n!=3]
  var ndata = data.where((n) => n != 3).map((n) => n * 2).toList();
  print("新しいデータは"+ndata.toString()+"です。");

  print("\nSample15");
  sale=[80,60,22,50,75];
  print("現在のデータは"+sale.toString()+"です。");

  print("最大のデータは"+max(sale).toString()+"です。");
  print("最小のデータは"+min(sale).toString()+"です。");

  print("データの合計は"+sum(sale).toString()+"です。");

  sss = List.from(sale);
  sss.sort();
  print("ソートされたデータは"+sss.toString()+"です。");

  var sss1 = List.from(sale);
  print("ソートされたデータは"+sss1.sorted((a, b) => a - b).toString()+"です。");

  sss2 = List.from(sale);
  print("ソートされたデータは"+sss2.sorted((a, b) => b - a).toString()+"です。");


  print("\nSample16");

  var data2=[
    ["東京",32,25],
    ["名古屋",28,21],
    ["大阪",27,20],
    ["京都",26,19],
    ["福岡",27,22],
  ];
  print("現在のデータは"+data2.toString()+"です。");

  for (var dat in data2){
    print("都市別データは"+dat.toString()+"です。");
    for (var d in dat) {
      stdout.write('$d\t');
    }
    print("");
  }

  print(data2[0][0].toString()+"の最高気温は"+data2[0][1].toString()+"最低気温は"+data2[0][2].toString()+"です。");

}
