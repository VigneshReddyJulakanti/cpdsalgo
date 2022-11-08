#include <iostream>
using namespace std;

int main(){
    int l,c;cin>>l>>c;
    int a[l],res[l];
    for(int i=0;i<l;i++){

        cin>>a[i];
    }
    for(int i=0;i<l;i++){
        res[i]=0;
        for(int j=i+1;j<(i+c+1);j++){
            res[i]+=a[j%l];
        }
    }
    if(c>0){ 
        for(int i=0;i<l;i++){
            cout<<res[i]<<" ";
        }
    }else{
        c = c*-1;
        for(int i=c-1;i<l+c-1;i++){
            cout<<res[l-(i%l)]<<" ";
        }
    }
    
}

