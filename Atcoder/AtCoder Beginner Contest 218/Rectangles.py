n=int(input())
input_list=[]
temp_list=[]
ans=0
for i in range(n):
    input_list.append(list(map(int,input().split())))
for i in range(n):
    for j in range(i+1,n):
        b=input_list[i][1]
        a=input_list[j][0]
        c=input_list[i][0]
        d=input_list[j][1]
        if ((a==c)or(b==d)):
            pass
        elif sorted([[c,b] ,[c,d] ,[a,d] ,[a,b]])  in temp_list:
            pass
        else:
         if (([a,b] in input_list )and( [c,d] in input_list)):
            ans+=1
            # print(f"{[c,b]} {[c,d]} {[a,d]} {[a,b]}")
            temp_list.append(sorted([[c,b] ,[c,d] ,[a,d] ,[a,b]]))

print(ans)

