#include <iostream>
using namespace std;

int main(){
    int n;
    cout << "Number of elements for the array: ";
    cin >> n;
    
    int a[n];
    
    cout << "Enter the elements for the array: ";
    
    for(int i=0; i<n; i++){
        cin >> a[i];
    }
    
    cout << "The array is: [ ";
    
    for(int i=0; i<n; i++){
        cout << a[i] << " ";
    }
    
    cout << "]" << endl;
    
   for (int i=0; i<n/2; i++){
       int temp = a[i];
       a[i] = a[n-i-1];
       a[n-i-1] = temp;
   }
   
   cout << "The reversed array is: [ ";
    
    for(int i=0; i<n; i++){
        cout << a[i] << " ";
    }
    
    cout << "]";
}
