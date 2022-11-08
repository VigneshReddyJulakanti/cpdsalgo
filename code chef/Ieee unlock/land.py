for n in range(int(input())):
    li1=[]
    li2=[]
    u=1
    for m in range(int(input())):
        
        li=list(input().split())
        if(u==0):
            continue
        p=1
        for y in range(1,int(li[0])):
            if(li[y] in li1):
                p=2
                break
            
        
        for l in range(1,int(li[0])):
            if p==1:
                if li[l] not in li1:
                    li1.append(li[l])
                else:
                    print(f"Case {n}: {0} {0} {0}")
                    u=0
                    break
            else:
                if li[l] not in li2:
                    li2.append(li[l])
                else:
                    print(f"Case {n}: {0} {0} {0}")
                    u=0
                    break
        if(u==0):
            continue
    if(u==1):
        li1=len(set(li1))
        li2=len(set(li2))
        print(f"Case {n}: {1} {li1} {li2}")
                

        
