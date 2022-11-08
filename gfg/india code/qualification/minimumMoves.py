
'''
#code
n=int(input())
for i in range(n):
    a,b=map(int,input().split())
    if(a<b):
        n=0
        x=0
        i=1
        while(n<=b):
            x=n
            n=a|i
            i+=1
        print(1+b-x)
    else:
        print(a-b)

'''
'''
#code
def x(a,b):
        n=0
        x=0
        i=1
        while(n<=b):
            x=n
            n=a|i
            i+=1
        return x
    
n=int(input())
for i in range(n):
    a,b=map(int,input().split())
    if(a<b):
        
        ansv=0
        ans=0
        while(a!=b):
            a=max(a+1,x(a,b))
            ans+=1
        
        print(ans)
    else:
        print(a-b)

'''

import numpy as np
def x(a,b):
        n=0
        x=0
        i=a
        l=np.inf
        
        while(i<=b+10):
            x=n
            temp=a|i
            if(temp<l and temp >b):
                l=temp
            if(temp<=b):
                n=temp
            i+=1
        return x,l

def fans(a,b):
        
        
        
        if(a==b):
            return 0
        if(a>b):
            return a-b
            
        t,y=x(a,b)
        return min(1+fans(max(a+1,t),b),1+fans(y,b))

        
    
    
n=int(input())
for i in range(n):
    a,b=map(int,input().split())
    print(fans(a,b))
    

