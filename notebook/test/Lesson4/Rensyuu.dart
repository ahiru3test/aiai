import 'dart:core';
import 'dart:io';

List<int> range(int start, int end, [int step = 1]) {
  return List<int>.generate((end - start) ~/ step + 1, (i) => start + i * step);
}

void main() {
  int a=3,b=2;
  if (a>b && b==1){
    print("a>b");
  } else {
    print("a<=b");
  }

  print("\nSample4");
  List l = List.generate(12, (index) => index);
  for (var i in l) {
    print((i+1).toString()+"月のデータです。");
  }

  print("\nSample6");
  List l1 = List.generate(5, (index) => index);
  List l2 = List.generate(3, (index) => index);
  for (var i in l1) {
    for (var j in l2) {
      print("iは"+(i).toString()+":jは"+(j).toString());
    }
  }

  print("");
  for (var i in range(1,12,1)) {
    for (var j in range(4,1,-1)) {
      print(i.toString()+"月"+j.toString()+"週");
    }
  }

  print("\nSample7");
  bool v=true;
  for (var _ in range(1,5,1)) {
    for (var _ in range(1,5,1)) {
      stdout.write(v?"*":"-");
      v = !v;
    }
    print("");
  }

  print("\nSample8");
  print("何月の処理で終了しますか？");
  String? s="";
  s = stdin.readLineSync();
  s = s==null?"0":s;
  for (var i in range(1,12,1)) {
    print(i.toString()+"月のデータです。");
    if (i==int.parse(s)) break;
  }
  print("");

  print("\nSample9");
  for (var i in range(1,12,1)) {
    if (i==int.parse(s)) continue;
    print(i.toString()+"月のデータです。");
  }
}
