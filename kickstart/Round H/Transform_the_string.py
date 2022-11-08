for n in range(int(input())):
    a=input()
    b=input()
    c=[]
    d=[]
    for i in a:
        c.append(ord(i))
    for i in b:
        d.append(ord(i))
    c=sorted(c)
    d=sorted(d)
    i=0
    j=0
    k=len(c)
    ans=[]
    l=len(d)

    prev=0
    next=0

    # ans+=abs(c[0]-d[0])
    mul=0

    while(i<k):
        if(l==1):
            ans.append(abs(c[i]-d[j]))
            i+=1
        else:
            if(j==l-1):
                ans.append(min(abs(c[i]-d[j]),abs(c[i]-d[j-1]),26-abs(c[i]-d[0])))
                i+=1
            elif(c[i]==d[j]):
                i+=1
            elif(j==0 and c[i]<d[j]):
                ans.append(min(abs(c[i]-d[j]),26-abs(c[i]-d[j-1])))
                i+=1
            elif(c[i]>d[j]):
                ans.append(min(abs(c[i]-d[j]),abs(c[i]-d[j-1]),abs(c[i]-d[j-2])))
                i+=1
            else:
                j+=1
    # print(ans)
    def boom(x):
        if(x>13):
         return 26-x
        else:
            return x
    ans=list(map(boom,ans))
    print(f"Case #{n+1}: {sum(ans)}")








            

    # while(i<k):
    #     if(c[i]==d[j]):
    #         i+=1
    #     if(j!=l-1):
    #           if((j==0)):
    #               ans.append(min(ord(c[i]-d[j]),ord(c[i]-d[j+1]),ord[c[i]-d[-1]-26]))
    #           elif(j==l-1):
    #               ans.append(min(ord(c[i]-d[j-1]),ord(c[i]-d[j]),ord[c[i]-d[-1]-26]))



    #     elif(c[i]>d[j]):
    #         ans.append(c[i]-d[j])
    #         i+=1
    #     elif((c[i]<d[j])):
    #         if(j<k-1):
    #              j+=1
    #         else:
    #             ans.append(d[j]-c[i])
    #             i+=1
    # for i in range(len(ans)):
    #     if(ans[i]>13):
    #         ans[i]=26-ans[i]
    # print(ans)
    # print(sum(ans))


    
            

