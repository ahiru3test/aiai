import 'dart:io';
//import 'dart:convert';
// import 'dart:await';

void main() {
  print("How old are you?");

  String? s1="";
  s1 = stdin.readLineSync();
  print("You are "+(s1??"unknown")+" years old.");

  print("How tall are you?");
  String? your_height="";
  your_height = stdin.readLineSync();

  print("How much do you weigh?");
  String? your_weight="";
  your_weight = stdin.readLineSync();

  print("Your height is "+(your_height??"0")+" cm.");
  print("Your weigh is "+(your_weight??"0")+" kg.");

}
