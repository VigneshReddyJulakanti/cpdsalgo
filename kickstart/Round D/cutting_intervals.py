'''
not working

# for t in range(int(input())):
#     n,c=map(int ,input().split())
#     dic={}
#     dl,dr=10**13+1,0
#     is_first=0
#     for i in range(n):
#         l,r=map(int ,input().split())
#         # if is_first==0:
#         #     for ii in range(l+1,r):
#         #         dic[ii]=1
#         #     is_first=1
#         # if l<dl:
#         #     dl=l
#         # if r>dr:
#         #     dr=r
#         for ii in range(l+1,r):
#             try :
#                 dic[ii]+=1
#             except:
#                 dic[ii]=1
#         iii=0
#         ans=n
#         for iii in sorted(list(dic.values())):
#             if iii==c:
#                 break
#             ans+=iii
#     print(f"Case #{t+1}: {ans}")
            


            










# for t in range(int(input())):
#     n,c=map(int ,input().split())
#     dic={}
#     li=[]
#     ans=n
#     for i in range(n):
#         l,r=map(int ,input().split())
#         for j in range(l+1,r):
#             li.append(j)
#             dic[j]=0
#     for i in li:
#         dic[i]+=1
#     li2=list(dic.values())
#     length_list=len(li2)
#     if length_list<=c:
#         ans+=sum(li2)
#     else:
#         ans+=sum(li2[:c])
#     print(f"Case #{t+1}: {ans}")
    
'''
        




'''

working for sample test case and test set 1

for t in range(int(input())):
    n,c=map(int ,input().split())
    list_Zero=[0]*(10**4+1)
    for i in range(n):
        l,r=map(int ,input().split())
        list_Zero[l+1]+=1
        list_Zero[r]-=1
    index_no=0
    prevno=0
    new_list=[]
    for i in list_Zero:
        prevno=prevno+i
        new_list.append(prevno)
        index_no+=1
        
    # print(new_list)
    # new_list=new_list.sort(reverse=True)
    # print(new_list)

    new_list=sorted(new_list)
    ans=n
    # lis_len=10**4-1
    for i in range(c):
        temp_num=new_list[-(i+1)]
        # print(f"i {i}")
        # print(f"temp_num {temp_num}")

        if(temp_num==0):break
        # print(f"i {i}")
        ans+=temp_num
        # c-=1
        # lis_len-=1
        # if c==0:break
    print(f"Case #{t+1}: {ans}")

'''






