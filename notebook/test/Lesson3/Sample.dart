import 'dart:core';
//import 'dart:io';

void main() {
  print("Sample1");
  int sale=10;
  print("売上は"+sale.toString()+"です。");

  print("\nSample2");
  sale=10;
  print("売上は"+sale.toString()+"です。");
  print("売上の値を変更します。");
  sale=20;
  print("売上は"+sale.toString()+"万円です。");

  print("\nSample3");
  String name="東京";
  sale=10;
  print(name+"売上は"+sale.toString()+"万円です。");

  print(name.runtimeType.toString() + "," + sale.runtimeType.toString());

  print("\nSample4");
  print(1+2);

  print("\nSample5,6");
  int price=50;
  int num=10;
  int total= price*num;
  print(price.toString()+","+num.toString()+","+total.toString());

  print(~(int.parse('0101',radix:2)));
  print(int.parse('0101',radix:2)|int.parse('0100',radix:2));
  print(int.parse('0101',radix:2)&int.parse('0100',radix:2));
  print(int.parse('0101',radix:2)^int.parse('0100',radix:2));
  print((int.parse('0101',radix:2))<<1);
  print((int.parse('0100',radix:2))>>1);


  print("\nSample7");
  num=10;
  String pic="〇";
  String graph = pic * num;
  print("売上："+graph.toString());
  print(num.toString()+"万円の売上があります。");
  print(num.toString()+"型変換して足す。");

}
