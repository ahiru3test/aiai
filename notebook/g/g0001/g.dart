import 'dart:core';

import 'test/test0001.dart';


void main(List<String> arguments) {
  test t=test();
  print("count:${test.count} name:${t.name}");
  test t2=test.setName("test2");
  print("count:${test.count} name:${t2.name}");
  test t3=test();
  print("count:${test.count} name:${t3.name}");
}
