#include <iostream>
using namespace std;

int main() {
	// your code goes here
	long long n,ab,ans,m=0;
	cin >> n;
	long long a[n];
	for(long long i=0;i<n;i++){
	    cin >> ab;
	    while(ab%5!=0){
	        ab--;
	    }
	    if (m<ab){
	        m=ab;
	    }
	    a[i]=ab;
	}
    // cout << endl << m << "m" << endl;
	long long anss[(m/5)],temp,tempans,prev=0;
	
	for(long long i=0;i<m/5;i++){
        // cout << "a";
	    tempans=0;
	    temp=5*(i+1);
	    while(temp%5==0){
	        temp=temp/5;
	        tempans++;
	    }
	    anss[i]=prev+tempans;
	    prev=prev+tempans;
	    
	    
	    
	    
	}
for(long long i=0;i<n;i++){
 
    if(a[i]<5){
        cout << 0 << endl;
        continue;
    }
    cout << anss[(a[i]/5)-1] << "\n";
}
	
	return 0;
}
