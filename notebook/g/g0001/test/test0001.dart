class test {
  static int count = 0;
  String name;

  test(): this.setName("UNKNOWN");
  test.setName(this.name) {
    count++;
    name = this.name;
  }
}