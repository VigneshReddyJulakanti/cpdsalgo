#include <iostream>
using namespace std;
int main(){
   
    int i=0,j=1,n;
    cin  >> n;
    int arr[n];
    
    while(j<=n){
        if(n%j==0){
            arr[i]=j;
            i++;

        }
        j++;


    }
    cout << i << "\n";

    for(int p=0;p<i;p++){
        cout << arr[p] << " ";
    }
    return 0;
}