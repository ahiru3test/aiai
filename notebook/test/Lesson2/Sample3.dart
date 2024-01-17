void main() {
  // 画面に2進数を出力する
  print("10進数の10は"+10.toString()+"です。");
  print("2進数の10は"+int.parse('10',radix:2).toString()+"です。");
  print("8進数の10は"+int.parse('10',radix:8).toString()+"です。");
  print("16進数の10は"+0x10.toRadixString(10).toString()+"です。");
  print("16進数のFは"+0xF.toRadixString(10).toString()+"です。");
}
