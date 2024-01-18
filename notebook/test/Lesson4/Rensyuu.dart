import 'dart:core';
import 'dart:io';

List<int> range(int start, int end, [int step = 1]) {
  return List<int>.generate((end - start) ~/ step + 1, (i) => start + i * step);
}

void main() {
  for (var i in range(1,10,1)){
    if(i%2==0) {
      print(i);
    }else{
      print(i*-1);
    }
  }

  for (var i in range(2,10,2)) print(i);

  for (var i in range(1,9,1)){
    for (var j in range(1,9,1)){
      stdout.write((i*j).toString()+"\t");
    }
    print("");
  }

  for (var i in range(1,5,1)) print("*"*i);  
}
