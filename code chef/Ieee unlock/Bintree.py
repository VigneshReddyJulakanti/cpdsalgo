for n in range(int(input())):
    a,b=map(int,input().split())
    ans=0
    while(a!=b):
        if(a>b):
            
                a=a//2
          
        else:
            
                b=b//2
           
        ans+=1
    print(ans)
