for _ in range(int(input())):
    n=int(input())
    li=list(map(int,input().split()))
    ans=0
    
    for i in range(n):
        ans+=(n-i)*i
    for i in range(n):
        if li[i]>i+1:
            k=li[i]-(i+1)
            ans-=(k*(k+1))/2
    print(ans)