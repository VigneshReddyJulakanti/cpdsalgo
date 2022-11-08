li=[]
for n in range(int(input())):
        # a=int(input())
        # ans=0
        # i=1
        
        # while(a>0):
        #     a=a-i
        #     i+=1
        #     ans+=1
        # ans=ans*2
        # print(ans)
                
        li.append(int(input()))
m=max(li)
boom=[0]
i=0
while True:
    boom.append(boom[i]+(i+1))
    i+=1
    if(boom[i]>=m):
        break

# print(f"li {li}")
# print(f"boom {boom}")
for j in li:
    ans=0
    first=0
    last=i-1
    while(last-first>=0):
        middle=int((first+last)/2)
        if(boom[middle]==j):
            ans=middle
            break
        if(boom[middle]>=j):
            last=middle-1
        else:
            first=middle+1
        ans=last+1
    # print(f" i {i}")
    # print(f"len {len(boom)}")
    # print(f"ans {j}  {ans}")
    print(2*ans)







    
