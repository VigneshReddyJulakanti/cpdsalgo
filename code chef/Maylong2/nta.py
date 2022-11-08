# def parent(i):
#     return (i-1)//2
# def left(i):
#     return 2*i+1
# def right(i):
#     return 2*i+2
    
# for _ in range(int(input())):
#     n=int(input())
#     for i in range(n-1):
#         a=input()
#     li=list(map(int,input().split()))
#     ans=[0 for i in range(n)]
#     def rec(arr,ind,n):
#         if ind>=n:
#             return -1
#         if left(ind)>=n and right(ind)>=n:
#             ans[ind]=-1
#             if(len(arr)==1):
#                 # print("barr",arr,"ind",ind)
#                 if arr[0]>li[ind]:
#                     arr.insert(0,li[ind])
#                 else:
#                     arr.append(li[ind])
#             else:
#                 arr.append(li[ind])
            
#             return -1
#         key=li[ind]
#         ml=rec(arr,left(ind),n)
        
#         mr=rec(arr,right(ind),n)
#         # print("arr",arr,"ind",ind)
#         l=0
#         r=len(arr)-1
#         mi=-1
#         if(r>0):
#             while(l<=r):
#             #    print("in while",l,r)
#                mid=(l+r)//2
#                if(key<arr[mid]):
#                    r=mid-1
#                else:
#                    l=mid+1
#             mi=min(key^arr[l],key^arr[r])
#             arr.insert(l,key)
#         else:
#             mi=key^arr[0]
#             if arr[0]>li[ind]:
#                     arr.insert(0,key)
#             else:
#                     arr.append(key)
#         if ml!=-1:
#             mi=min(mi,ml)
#         if mr!=-1:
#             mi=min(mi,ml)
#         ans[ind]=mi
            
#         return mi
#     rec([],0,n)
#     print(*ans)
            
        
            
        
# import sys
# sys.setrecursionlimit(100000)  
    
# for _ in range(int(input())):
#     n=int(input())
   
#     child={}
    
#     for i in range(n-1):
#         a,b=map(int,input().split())
#         if a in child:
#             child[a].append(b)
#         else:
#             child[a]=[b]
        

#     li=list(map(int,input().split()))
#     ans=[0 for i in range(n)]
#     def rec(ele,arr):

#         if ele not in child:
#             ans[ele-1]=-1
#             arr.append(li[ele-1])
#             return -1
#         tem=[]
#         # print("ele",ele)
#         for i in child[ele]:
#             tem.append(rec(i,arr))
#         key=li[ele-1]
#         l=0
#         r=len(arr)-1
#         mi=-1
#         if(r>0):
#             while(l<=r):
#             #    print("in while",l,r)
#                mid=(l+r)//2
#                if(key<arr[mid]):
#                    r=mid-1
#                else:
#                    l=mid+1
#             mi=min(key^arr[l],key^arr[r])
#             arr.insert(l,key)
#         else:
#             mi=key^arr[0]
#             if arr[0]>key:
#                     arr.insert(0,key)
#             else:
#                     arr.append(key)
#         for i in tem:
#             if i!=-1:
#                 mi=min(mi,i)
#         ans[ele-1]=mi
#         return mi
#     rec(1,[])
#     print(*ans)
            





   

        
    #     key=li[ind]
    #     ml=rec(arr,left(ind),n)
        
    #     mr=rec(arr,right(ind),n)
    #     # print("arr",arr,"ind",ind)
    #     l=0
    #     r=len(arr)-1
    #     mi=-1
    #     if(r>0):
    #         while(l<=r):
    #         #    print("in while",l,r)
    #            mid=(l+r)//2
    #            if(key<arr[mid]):
    #                r=mid-1
    #            else:
    #                l=mid+1
    #         mi=min(key^arr[l],key^arr[r])
    #         arr.insert(l,key)
    #     else:
    #         mi=key^arr[0]
    #         if arr[0]>li[ind]:
    #                 arr.insert(0,key)
    #         else:
    #                 arr.append(key)
    #     if ml!=-1:
    #         mi=min(mi,ml)
    #     if mr!=-1:
    #         mi=min(mi,ml)
    #     ans[ind]=mi
            
    #     return mi
    # rec([],0,n)
    # print(*ans)
            
        
            
        
        
        
import sys
sys.setrecursionlimit(100000)  
    
for _ in range(int(input())):
    n=int(input())
   
    child={}

    dren=[]
    there=set(1)

    
    for i in range(n-1):
        a,b=map(int,input().split())
        if a in child:
            child[a].append(b)
        else:
            child[a]=[b]
        

    li=list(map(int,input().split()))
    ans=[0 for i in range(n)]
    def rec(ele,arr):

        if ele not in child:
            ans[ele-1]=-1
            arr.append(li[ele-1])
            return -1
        tem=[]
        # print("ele",ele)
        for i in child[ele]:
            tem.append(rec(i,arr))
        key=li[ele-1]
        l=0
        r=len(arr)-1
        mi=-1
        if(r>0):
            while(l<=r):
            #    print("in while",l,r)
               mid=(l+r)//2
               if(key<arr[mid]):
                   r=mid-1
               else:
                   l=mid+1
            mi=min(key^arr[l],key^arr[r])
            arr.insert(l,key)
        else:
            mi=key^arr[0]
            if arr[0]>key:
                    arr.insert(0,key)
            else:
                    arr.append(key)
        for i in tem:
            if i!=-1:
                mi=min(mi,i)
        ans[ele-1]=mi
        return mi
    rec(1,[])
    print(*ans)