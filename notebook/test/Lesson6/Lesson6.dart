import 'dart:core';

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

}

