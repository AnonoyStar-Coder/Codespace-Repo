#include <iostream>
using namespace std;

class Person {

  private:

  string name;
  int age;

  public:

  void set_det(const string P_name; age P_age){
    name = P_name;
    age = P_age;
  }
  
  void Display(){
    cout << "Name: " << name << endl;
    cout << "Age: " << age << endl;
  }
};

int main(){
  
  Person P;
  P.set_det("Ram"; 45);

  P.Display();

  return 0;
}
