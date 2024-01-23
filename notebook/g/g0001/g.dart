import 'dart:core';

import 'test/test0001.dart';
import 'test/TSingleton2.dart';

void main(List<String> arguments) {
  test t=test();
  print("count:${test.count} name:${t.name}");
  test t2=test.setName("test2");
  print("count:${test.count} name:${t2.name}");
  test t3=test();
  print("count:${test.count} name:${t3.name}");

  TSingleton2 ts2=TSingleton2.instance;
  print("${ts2.n}\t${TSingleton2.count}");
}
