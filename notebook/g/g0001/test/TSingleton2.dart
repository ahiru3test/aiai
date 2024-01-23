import 'dart:core';

///シングルトンパターンのサンプルクラス
class TSingleton2{
  //シングルトンインスタンスの作成
  TSingleton2._() { _count++; }
  ///シングルトンのインスタンス
  static final instance = TSingleton2._(); 
  //static宣言部
  static int _count = 0;
  static int get count => _count;
  //クラス宣言部
  int n=0;
}

///テストmain
void main(List<String> arguments){
  TSingleton2 ts= TSingleton2.instance;
  print("count:${TSingleton2.count}, n:${ts.n}");
  ts.n++;
  print("count:${TSingleton2.count}, n:${ts.n}");
  TSingleton2 ts2= TSingleton2.instance;
  print("count:${TSingleton2.count}, n:${ts2.n}");
  ts2.n++;
  print("count:${TSingleton2.count}, n:${ts2.n}");
}
