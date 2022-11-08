
ans=0
for n in range(int(input())):
    
    
    x1,y1,x2,y2,x3,y3=map(int , input().split())
    # if ((x1==x2 or x2==x3 or x3==x1) and (y1==y2 or y2==y3 or y3==y1)):
    #     ans+=1
    if(x1==x2==x3) or (y1==y2==y3):
        continue
    a=((x1-x2)**2+(y1-y2)**2)
    b=((x3-x2)**2+(y3-y2)**2)
    c=((x1-x3)**2+(y1-y3)**2)
    list=[a,b,c]
    if(a==0 or b==0 or c==0):
        continue
    list=sorted(list)
    # print(list[0])
    # print(list[1])
    # print(list[2])
    # print((((list[0])**2)+((list[1])**2))**0.5)
    # print(((list[2])))
    if(int(((list[0])+((list[1]))))==int((list[2]))):
        # print(f"n {n}")
        ans+=1

print(ans)
