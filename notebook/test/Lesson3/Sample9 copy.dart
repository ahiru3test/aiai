import 'dart:io';
//import 'dart:convert';
// import 'dart:await';

void main() {
  print("\nSample9");
  print("値1を入力してください。");
  String? s1="";
  s1 = stdin.readLineSync();
  double num1 = double.parse(s1 == null ? "0" : s1 );

  print("値2を入力してください。");
  String? s2="";
  s2 = stdin.readLineSync();
  double num2 = double.parse(s2 == null ? "0" : s2 );

  double num3 = num1 + num2;
  print(num3);

  print("整数値化すると");
  print((num1.toInt() + num2.toInt()).toString());

}
