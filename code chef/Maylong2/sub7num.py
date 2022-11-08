# # # def div(n):
     
# # #     # if n==0 or n==7:
# # #     #     return True
# # #     # if n<10:
# # #     #     return False
# # #     # k=str(n)
# # #     if n%7==0:
# # #         return True
# # #     return False
  
# # #     return div(int(k[:-1])-2*int(k[-1]))
# # for _ in range(int(input())):
# #     n=int(input())
# #     li=input().split()
# #     ans=[0]
# #     temp=[]
    
# #     def rec(ind,n,s):
# #         # print("".join(temp))
# #         if len(s)!=0:
# #             # print("boom  "+"".join(temp))
            
# #             if int(s)%7==0:
# #                 ans[0]=(ans[0]+1)
        
# #         for i in range(ind,n):
# #             rec(i+1,n,s+li[i])
            
            
# #     rec(0,n,"")
# #     print(ans[0]%((10**9)+7))
            
    
#     # def div(n):
     
# #     # if n==0 or n==7:
# #     #     return True
# #     # if n<10:
# #     #     return False
# #     # k=str(n)
# #     if n%7==0:
# #         return True
# #     return False
  
# #     return div(int(k[:-1])-2*int(k[-1]))
# for _ in range(int(input())):
#     n=int(input())
#     li=input().split()

    
#     def rec(ind,n,s):
#         # print("".join(temp))
#         temp=0
      
#         if len(s)!=0:
#                 s=int(s)%7
#                 if s==0:
#                     temp+=1
#                     s=""
#                 else:
                    
#                     s=str(s)
#         for i in range(ind,n):

            
            
#             temp+=rec(i+1,n,s+li[i])
#         return temp%((10**9)+7)
            
    
#     print(rec(0,n,"")%((10**9)+7))
import sys
sys.setrecursionlimit(3000000)        
# for _ in range(1):
for _ in range(int(input())):
    n=int(input())
    # n=300000
    li=input().split()
    # li=["300000" for k in range(300000)]
    # print(li)
    
    def rec(ind,n,s):
      
        temp=0
      
        if len(s)!=0:
                print("s",s)
                s=int(s)%7

                if s==0:
                    # print("s",s)
                    temp+=1
                    s=""
                else:
                    
                    s=str(s)
        # for i in range(ind,n):
        if (ind>=n):
            return temp
            
            
        temp=temp%((10**9)+7)+rec(ind+1,n,s+li[ind])
        if(ind+1<n):
            temp=temp%((10**9)+7)+rec(ind+2,n,s+li[ind+1])
        
        return temp%((10**9)+7)
            
    
    print(rec(0,n,"")%((10**9)+7))
            
    