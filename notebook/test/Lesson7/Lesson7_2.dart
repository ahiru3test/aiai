// import 'dart:async';
import 'dart:core';
// import 'dart:io';


void main(){
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


  print("");
  // #通常の関数
  var inches = [9,5.5,6,4,5,6.5,10];
  var cms=[];

  for (var inch in inches.where(largerThan5_2)){
    cms.add(inch *2.54);
  }

  print(cms);

  // #lambda
  cms=[];
  for(var inch in inches.where((inch) => inch>=5)){
    cms.add(inch *2.54);
  }
  print(cms);

  // #リスト内包
  print([for (var inch in inches) if (inch >=5) inch*2.54]);


  print("\nSample10");
  var str = "aaa";
  var newfunc = deco(printmsg);
  newfunc(str);

}

bool largerThan5(int inch){
    return inch >=5;
}

bool largerThan5_2(num inch){
    return inch >=5;
}

Function deco(Function func) {
  Function wrapper(String x) {
    //引数に文字列を追加します。
    String wx = "---" + x + "---";
    return func(wx);
  }
  return wrapper;
}

void printmsg(String x) {
  print("$xを入力しました。");
}
