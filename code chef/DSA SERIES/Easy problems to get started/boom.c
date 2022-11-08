#include<stdio.h>
int main(){
    int nlamps;
    scanf("%d",&nlamps);
    int arr[nlamps];
    for(int i=0;i<nlamps;i++){
        scanf("%d",&arr[i]);
    }
    int maxnum=arr[0],count=0;
        for(int i=0;i<nlamps;i++){
      if(arr[i]>maxnum){
          maxnum=arr[i];
      }
    }
            for(int i=0;i<nlamps;i++){
      if(arr[i]==maxnum){
          count++;
      }
    }
    printf("%d",count);
    return 0;
    
}