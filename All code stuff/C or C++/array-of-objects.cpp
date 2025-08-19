#include <iostream>

using namespace std;

class student {
  int marks[5];
  public:

  void inputMarks(){
    cout << "Enter the 5 subject marks: ";
    for(int i=0; i<5; i++){
      cin >> marks[i];
    }
  }
  void displayMarks(){
    cout << "Marks: ";
    for(int i=0; i<5; i++){
      cout << marks[i] << " ";
    }
    cout << endl;
  }
  int totalMarks(){
    int t=0;
    for(int i=0; i<5; i++){
      t += marks[i];
    }
      return t;
    }
};
int main(){
  student s[3];

  for(int i=0; i<3; i++){
    cout << "Enter marks for student " << i+1 << endl;
    s[i].inputMarks();
  }

  for(int i=0; i<3; i++){
    cout << "Marks for student " << i+1 << endl;
    s[i].displayMarks();
    cout << "Total marks: " << s[i].totalMarks() << endl;
  }

  return 0;
}
