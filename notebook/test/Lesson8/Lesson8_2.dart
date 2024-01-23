import 'dart:core';


void main(){
  var pr = Customer("鈴木",23,"mmm@nnn.nn.jp","xxx-xxx-xxxx");
  var nm = pr.getName();
  var ag = pr.getAge();
  var ad = pr.getAdr();
  var tl = pr.getTel();

  print("${nm}さんは${ag}才です。");
  print("アドレスは${ad}電話番号は${tl}です。");
}

class Person {
  String name;
  int age;

  Person(this.name, this.age);

  String getName() {
    return this.name;
  }

  int getAge() {
    return this.age;
  }
}

class Customer extends Person {
 String adr;
 String tel;

 Customer(String name, int age, this.adr, this.tel) : super(name, age);

 String getName() {
    return "顧客："+name;
 }

 String getAdr() {
    return adr;
 }

 String getTel() {
    return tel;
 }
}

