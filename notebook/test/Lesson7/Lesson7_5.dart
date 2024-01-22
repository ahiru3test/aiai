import 'dart:core';

List<int> range(int start, int end, [int step = 1]) {
  return List<int>.generate((end - start) ~/ step + 1, (i) => start + i * step);
}

var a=0;

void main(){
  print("\nSample12");
  a=0;
  for ( var _ in range(1,5)){
    func();
  }
}

void func(){
  var b=0;
  print("変数aは"+a.toString()+"変数bは"+b.toString());

  a=a+1;
  b=b+1;
}