import 'dart:core';

void main(){
  var n = makeX(3);
  print(n.first);
  print(n.elementAt(1));
  print(n.elementAt(2));
  try {
    print(n.elementAt(3));
  } catch (e) {
    print("エラーが発生しました。");
  }
}

Iterable<int> makeX(int x) sync* {
  int n = 0;
  while (n < x) {
    yield n;
    n++;
  }
}
