import 'dart:core';

void main(List<String> arguments){
  print("\nSample1");
  Person pr;

  pr = Person();
  pr.name="鈴木";
  pr.age=23;

  print("${pr.name}さんは${pr.age}才です。");

  Person pr2 = Person();
  pr2.name="佐藤";
  pr2.age=38;

  print("${pr2.name}さんは${pr2.age}才です。");


  Person pr1_2 = Person();
  print("${pr1_2.name}さんは${pr1_2.age}才です。");
  Person2 pr2_2 = Person2();
  print("${pr2_2.name}さんは${pr2_2.age}才です。");


  print("\nSample3");
  Person pr3 = Person.withNameAndAge("鈴木",23);
  print("${pr3.name}さんは${pr3.age}才です。");


  print("\nSample4");
  Person3 pr4_1 = Person3.withNameAndAge("鈴木",23);
  Person3 pr4_2 = Person3.withNameAndAge("佐藤",38);
  print("${pr4_1.name}さんは${pr4_1.age}才です。");
  print("${pr4_2.name}さんは${pr4_2.age}才です。");
  print("合計人数は${Person3.count}です。");

}

class Person {
  String name="";
  int age=0;

  Person();
  // Person() : name="",age=0;
  Person.withNameAndAge(this.name,this.age);
}
class Person2 {
  String name;
  int age;

  Person2() : name="",age=0;
  Person2.withNameAndAge(this.name,this.age);
}
class Person3 {
  static int count=0;
  static init() {
    count++;
  }

  String name="";
  int age=0;

  Person3() {
    init();
  }
  Person3.withNameAndAge(this.name, this.age){
    init();
  }
}
