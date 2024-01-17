import 'dart:io';
//import 'dart:convert';
// import 'dart:await';

void main() {
  print("\nSample8");
  print("値を入力してください。");
  String? s="";
  s = stdin.readLineSync();
  print(s);


  
  // await stdin
  //     .transform(UTF8.decoder)
  //     .transform(const LineSplitter())
  //     .forEach((line) {
  //         print(line);
  //     });
  // print("DONE!");


  // print("START!");
  // for line iter(sys.stdin.readline, ""):
  //     print line;
  //   print "DONE!"

  // String? s="";
  // s = stdin.readLineSync();
  // int n = int.parse(s==null?"0":s);
  // print(n.toString()+"が入力されました。");

  // if (s == null) {
  //   ;

  // } else {

  // }
  // int n = int.parse(s.isEmpty ? '0' : int.parse(s));
  // print(n.toString()+"が入力されました。");
}
