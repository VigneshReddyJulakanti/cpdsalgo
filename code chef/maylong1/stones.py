def ans(a,b):
    if a<0 or b<0 :
        return 10**9
    
    if a%3==0 or b%3==0:
        return 0
    # print(a,b,abs(a-b))
    k=abs(a-b)
    if k < a and k<b:
        return 1+min(ans(abs(a-b),b),ans(a,abs(a-b)))
    elif k<a:
        return 1+ ans(k,b)
    else:
        return 1+ans(a,k)
    
for _ in range(int(input())):
    a,b=map(int,input().split())
    print (ans(a,b))
        
        
        