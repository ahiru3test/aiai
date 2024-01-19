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
  print("現在のデータは",sale,"です。");

  k="金沢";
  if ( k in sale) {
    print(k+"のデータは"+sale[k].toString()+"です。");
  } else {
    print(k+"のデータはみつかりませんでした。");
  }

}

