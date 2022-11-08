#include <iostream>
using namespace std;
int main(){
    int a,i;
    cin >> a;
    for(i=0;i<a;i++){
        for(int j=0;j<a-1-i;j++){
            cout << " ";
        }
        for(int j=0;j<i+1;j++){
            cout << "*";
        }
        cout << "\n";

    }
    return 0;
}