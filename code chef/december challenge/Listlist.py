for n in range(int(input())):
    a=int(input())
    b=list(map(int ,input().split()))
    if(a<2):
        print(0)
        continue
    c=set(b)
    if(len(c)==1):
        print(0)
        continue

    if(len(c)==len(b)):
        print(-1)
        continue
    b=sorted(b)
    k=b[0]
    cou=0
    tlen=0
    p=0
    for i in b:
        if(i==k):
            tlen+=1
        else:
            if(tlen>cou):
                cou=tlen
            tlen=1
            k=i
        if(p==len(b)-1):
                if(tlen>cou):
                  cou=tlen
        p+=1
                


    # for i in c:
    #     if(b.count(i)>cou):
    #         cou=b.count(i)
    #         val=i

    

    print(a-1-cou+2)
    