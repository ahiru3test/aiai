import 'dart:core';

class TSingreton{
  static final TSingreton _tsingreton = TSingreton._internal();
  static int count=0;
  int n=0;

  factory TSingreton(){
    return _tsingreton;
  }

  TSingreton._internal(){
    count++;
  }
}

void main(List<String> arguments){
  TSingreton ts= TSingreton();
  print("count:${TSingreton.count}, n:${ts.n}");
  ts.n++;
  print("count:${TSingreton.count}, n:${ts.n}");
  TSingreton ts2= TSingreton();
  print("count:${TSingreton.count}, n:${ts2.n}");
  ts2.n++;
  print("count:${TSingreton.count}, n:${ts2.n}");
}
