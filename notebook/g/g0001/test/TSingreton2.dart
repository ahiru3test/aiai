import 'dart:core';

///シングルトンパターンのサンプルクラス
class TSingreton2{
  //シングルトンインスタンスの作成
  TSingreton2._() { _count++; }
  static final instance = TSingreton2._();
  //static宣言部
  static int _count = 0;
  static int get count => _count;
  //クラス宣言部
  int n=0;
}

///テストmain
void main(List<String> arguments){
  TSingreton2 ts= TSingreton2.instance;
  print("count:${TSingreton2.count}, n:${ts.n}");
  ts.n++;
  print("count:${TSingreton2.count}, n:${ts.n}");
  TSingreton2 ts2= TSingreton2.instance;
  print("count:${TSingreton2.count}, n:${ts2.n}");
  ts2.n++;
  print("count:${TSingreton2.count}, n:${ts2.n}");
}
