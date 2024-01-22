import 'dart:core';

List<int> range(int start, int end, [int step = 1]) {
  return List<int>.generate((end - start) ~/ step + 1, (i) => start + i * step);
}


void main(){
  //普通に
  var start=3, end=9;
  for (var n in range(start,end)){
    print(n);
  }


  //ジェネレータ
  var n = makex(start);
  var it = n.iterator;
  while (it.moveNext()){
    if(it.current >end) {
      break;
    }
    print(it.current);
  }

}

Iterable<int> makex(int x) sync* {
  while (true) {
    // yield文で値を返します。
    yield x;
    x += 1;
  }
}
