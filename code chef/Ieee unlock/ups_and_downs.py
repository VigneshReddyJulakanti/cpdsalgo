for n in range(int(input())):
    nn=int(input())
    li=list(map(int,input().split()))
    li=sorted(li)
    # for i in range(nn):
    #     for j in range(nn-i):
    #         if(li[j]>li[j+1]):
    #             temp=li[j]
    #             li[j]=li[j+1]
    #             li[j+1]=temp
    mid=nn//2
    for i in range(mid):
        print(li[i],end=" ")
        print(li[nn-1-i],end=" ")
    if(nn%2!=0):
        print(li[mid],end="")

    print("")

