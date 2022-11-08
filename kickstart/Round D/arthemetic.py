for k in range(int(input())):
    a00,a01,a02=map(int , input().split())
    a10,a12=map(int , input().split())
    a20,a21,a22=map(int , input().split())
    adl=(a00+a22)/2
    adr=(a02+a20)/2
    av=(a01+a21)/2
    ah=(a10+a12)/2
    li=[adl,adr,av,ah]
    dictt={}
    ans=0

    for i in li:
        dictt[i]=0
        if i.is_integer():
                
            
            for j in li:

             if i==j:
                dictt[i]=dictt[i]+1
    
    # print(dictt)
    ans+=int(max(list(dictt.values())))
    if(a01==(a00+a02)/2):
        ans+=1
    if(a10==(a00+a20)/2):
        ans+=1
    if(a21==(a20+a22)/2):
        ans+=1
    if(a12==(a02+a22)/2):
        ans+=1
    print(f"Case #{k+1}: {ans}")
    # ans=0
    # if adl==adr==av==ah:
    #     ans+=4
    # elif adl==adr==av or 



