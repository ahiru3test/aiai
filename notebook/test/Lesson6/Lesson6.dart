import 'dart:core';
import 'dart:io';

void main(){
  var t=[1,2,3];
  print(t.runtimeType);

  print("\nSample1");
  var sale={"東京":80, "名古屋":60,"京都":22,"大阪":50,"福岡":75};
  print("現在のデータは"+sale.toString()+"です。");

  var k="京都";
  print(k+"のデータは"+sale[k].toString()+"です。");


  print("\nSample2");
  sale={"東京":80, "名古屋":60,"京都":22,"大阪":50,"福岡":75};
  print("現在のデータは"+sale.toString()+"です。");

  k="金沢";
  if (sale.containsKey(k)) {
    print(k+"のデータは"+sale[k].toString()+"です。");
  } else {
    print(k+"のデータはみつかりませんでした。");
  }

  print("\nSample3");
  sale={"東京":80, "名古屋":60,"京都":22,"大阪":50,"福岡":75};
  print("現在のデータは"+sale.toString()+"です。");

  k="横浜";
  if (sale.containsKey(k)) {
    print(k+ "のデータはすでに存在しています。");
  } else {
    var d=40;
    sale[k] = d;
    print(k+"のデータとして"+sale[k].toString()+"を追加しました。");
  }
  print("現在のデータは"+sale.toString()+"です。");

  k="京都";
  if (sale.containsKey(k)) {
    print(k+ "のデータは"+sale[k].toString()+"です。");
    var d=99;
    sale[k] = d;
    print(k+"のデータは"+sale[k].toString()+"に変更されました。");
  } else {
    print(k+"のデータはみつかりませんでした。");
  }
  print("現在のデータは"+sale.toString()+"です。");

  k="名古屋";
  if (sale.containsKey(k)) {
    print(k+"のデータは"+sale[k].toString()+"です。");
    sale.remove(k);
    print("データを削除しました。");
  } else {
    print(k+"のデータはみつかりませんでした。");
  }
  print("現在のデータは"+sale.toString()+"です。");

  print("\nSample4");
  sale={"東京":80, "名古屋":60,"京都":22,"大阪":50,"福岡":75};
  print("現在のデータは"+sale.toString()+"です。");

  print("キーを表示します。");
  for (var k in sale.keys){
    stdout.write(k+"\t");
  }
  print("");

  print("値を表示します。");
  for (var v in sale.values){
    stdout.write(v.toString()+"\t");
  }
  print("");

  print("キーと値を表示します。");
  for (var e in sale.entries){
    stdout.write(e.key+","+e.value.toString()+"\t");
  }
  print("");


  print("\nSample5");
  var sale1={"東京":80, "名古屋":60,"京都":22};
  var sale2={"京都":100,"大阪":50,"福岡":75};
  print("現在のデータは"+sale1.toString()+"です。");
  print("現在のデータは"+sale2.toString()+"です。");

  print("1を2で更新します。");

  sale1.addAll(sale2);

  print("1のデータは"+sale1.toString()+"です。");


  print("\nSample6");
  var city={"東京", "名古屋","京都","大阪","福岡"};
  print("現在のデータは"+city.toString()+"です。");

  // var d=input("追加するデータを入力してください。");
  var d="横浜";
  if (city.contains(d)) {
    print(d+"のデータはすでに存在しています。");
  } else {
    city.add(d);
    print(d+"を追加しました。");
  }
  print("現在のデータは"+city.toString()+"です。");

  d="京都";
  if (city.contains(d)) {
    city.remove(d);
    print(d+"を削除しました。");
  } else {
    print(d+"のデータはみつかりませんでした。");
  }
  print("現在のデータは"+city.toString()+"です。");

  print("\nSample7");
  var cityA={"東京","名古屋","京都","大阪"};
  var cityB={"京都","大阪","福岡"};

  print("Aの都市名は"+cityA.toString()+"です。");
  print("Bの都市名は"+cityB.toString()+"です。");

  print("共通するデータは"+(cityA.intersection(cityB)).toString()+"です。");
  print("Aのみのデータは"+(cityA.difference(cityB)).toString()+"です。");
  print("Bのみのデータは"+(cityB.difference(cityA)).toString()+"です。");
  print("すべてのデータは"+(cityA.union(cityB)).toString()+"です。");


  print("\nRensyuu");
  var data={};
  data["a1"]=10;
  print(data);
  data.remove("a1");
  print(data);

  var data2=Set();
  data2.add("a1");
  print(data2);
  data2.remove("a1");
  print(data2);

  print(data.runtimeType.toString()+"\t"+data2.runtimeType.toString());

}
