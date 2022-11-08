#include <iostream>
using namespace std;
int main(){
    int n , a,b=-1;
    cin >> n >> a;
    int arr[n];
    for(int i=0;i<n;i++){
        cin >> arr[i];
    }
    
    for(int i=0;i<n;i++){
        if(arr[i]==a){
            cout << 1;
            b=1;
        }

    }
    if(b!=1){
        cout << "−1";

    }
    return 0;
    
}