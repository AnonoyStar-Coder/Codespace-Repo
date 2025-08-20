// Online C++ compiler to run C++ program online
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
    
    cout << "]";
    
    for(int i=0; i<n-1; i++){
        for (int j=0; j < n-i-1; j++){
            if (a[j] < a[j+1]){
                int temp = a[j];
                a[j] = a [j+1];
                a[j+1] = temp;
            }
        }
    }
    
    cout << endl << "The array in descending order is: [ ";
    
    for(int i=0; i<n; i++){
        cout << a[i] << " ";
    }
    
    cout << "]";
}
