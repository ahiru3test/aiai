import 'dart:core';

void main(){
  print("\nSample10");
  var str = "aaa";
  var newfunc = deco(printmsg);
  newfunc(str);
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
