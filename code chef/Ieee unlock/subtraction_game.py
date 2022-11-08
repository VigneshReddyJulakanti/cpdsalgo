# for n in range(int(input())):
#     a=input()
#     li=list(map(int,input().split()))
#     while(len(li)!=1):
#         li=sorted(li)
#         li[-1]-=li[0]
#         li=set(li)
#         li=list(li)
#     print(li[0])


# for n in range(int(input())):
#     a=int(input())
#     li=list(map(int,input().split()))
#     m=min(li)

#     while(True):
#         f=1
#         for i in li:
#             if(i%m!=0):
#                 f=0
#                 break
#         if(f==1):
#             print(m)
#             break
#         m-=1


# for n in range(int(input())):
#     i=int(input())-2
#     li=list(map(int,input().split()))
#     li=sorted(li)
#     ans=li[-2]
#     m=min(li)
#     while i>-2:
#         ans=min(ans,li[i+1]-ans)
#         while(li[i]>ans and i>=0):
#             i-=1
#         if(i==-1):
#             ans=min(ans,li[i+1]-ans)
#             break

#     print(ans)
def gcd(a,b,c):
    if c==1:
        return 1
    if(a%c==0 and b%c==0):
        return c
    else: 
        return gcd(a,b,c-1)
for n in range(int(input())):
    i=int(input())
    li=list(map(int,input().split()))
    li=sorted(li)
    gstart=gcd(li[0],li[1],min(li[0],li[1]))
    ans=gstart
    for j in range(i-2):
        
        ans=gcd(gstart,li[j+2],min(gstart,li[j+2]))
        gstart=ans
    print(ans)
        






