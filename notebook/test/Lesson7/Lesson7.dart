import 'dart:core';
import 'dart:io';


void main(){
  print("\nSample1");
  sell();
  sell();


  print("\nSample3");
  sell3("東京");
  sell3("大阪");


  print("\nSample4");
  var shop="東京";
  sell3(shop);


  print("\nSample5");
  shop="東京";
  var num=5;
  sell5(shop,num);

  print("\nSample6");
  func(d: 10, c: 2, b: 3, a: 1);
  func(c:2);

  func2({"name":"aaa","age":17,"height":170.2});


  print("\nSample7");
  List s = sell7();
  print("販売完了："+s[0].toString()+s[1].toString()+s[2].toString());


  print("\nSample8");
  List<Function> list = [append, update, delete];
  stdout.write("操作番号を入力してください。（０～２）:");
  int res = int.parse(stdin.readLineSync()!);
  if (res >= 0 && res < list.length) {
    list[res]();
  }


  print("\nSample9");
  List<int> data = [1, 2, 3, 4, 5];

  // A.通常の関数
  int f(int x) {
    return x * 2;
  }

  for (int d in data.map(f)) {
    print(d);
  }

  // B.ラムダ
  for (int d in data.map((int x) => x * 2)) {
    print(d);
  }

  // C.リスト内包
  for (int d in [for (int x in data) x * 2]) {
    print(d);
  }

}

void sell(){
    print("販売が行われました。");
}
void sell3(String place){
    print(place+"支店の販売が行われました。");
}
void sell5(String place,int num){
    print(place+"支店で"+num.toString()+"万円の販売が行われました。");
}

void func({int a=0,int b=0,int c=0,int d=0}){
  print(a.toString()+b.toString()+c.toString()+d.toString());
}
void func2(Map<String, dynamic> kargs){
  print(kargs);
}

List<int> sell7() {
    var y=2018;
    var m=10;
    var d=1;
    print("${y}年${m}月${d}日に販売が行われました。");

    return [y,m,d];
}

void append() {
  print("データを追加します。");
}
void update() {
  print("データを変更します。");
}
void delete() {
  print("データを削除します。");
}
