import 'dart:core';
import 'dart:io';

List<int> range(int start, int end, [int step = 1]) {
  return List<int>.generate((end - start) ~/ step + 1, (i) => start + i * step);
}
void main(){
  print("");
}
