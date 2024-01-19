import 'dart:core';
// import 'dart:io';
import 'package:collection/collection.dart';
import 'package:quiver/iterables.dart';
// import 'package:zip/zip.dart';

int sum(List<int> list) {
 return list.reduce((value, element) => value + element);
}

void main(){
  print("");
  var data=[74,85,69,77,81];
  print("テストの点は"+data.toString()+"です。");
  print("最高点は"+max(data).toString()+"です。");
  print("最低点は"+min(data).toString()+"です。");

  print("平均点は"+(sum(data)/data.length).toString()+"です。");

  print("");
  data=[74,85,69,77,81];
  print("テストの点は"+data.toString()+"です。");
  var data1 = List.from(data);

  print("昇順は"+data1.sorted((a, b) => a - b).toString()+"です。");
  print("降順は"+data1.sorted((a, b) => b - a).toString()+"です。");
  print("dataは"+data.toString()+"です。");


  print("");
  data=[74,85,69,77,81];
  print("テストの点は"+data.toString()+"です。");
  // var data2=[n for n in data if n>=80];
  // var data2 = data.where((n) => n != 3).map((n) => n * 2).toList();
  var data2 = data.where((n) => n >= 80).map((n) => n).toList();

  print("８０点以上は"+data2.toString()+"です。");
  print("８０点以上の人数は"+data2.length.toString()+"人です。");

  print("");
  var city=['東京','名古屋','大阪','京都','福岡'];
  var maxk=[32,28,27,26,27];
  var mink=[25,21,20,19,22];

  print("都市名データは"+city.toString()+"です。");
  print("最高気温データは"+maxk.toString()+"です。");
  print("最低気温データは"+mink.toString()+"です。");

  // for (var p in zip(city,maxk,mink)) {
  //   print(p[0]+"の最高気温は"+p[1]+"最低気温は"+p[2]+"です。");
  // }

  print("最高気温でソートしてみる");
  var zzz = IterableZip([maxk,city,mink]);
  
  for (var p in zzz.sorted((a, b) => (a[0] as int).compareTo(b[0] as int))){
    print(p[1].toString()+"の最高気温は"+p[0].toString()+"最低気温は"+p[2].toString()+"です。");
  }

}
