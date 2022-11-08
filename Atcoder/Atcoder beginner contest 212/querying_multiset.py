n=int(input())
balls_list=[]
k=0
min_ind=0
for i in range(n):
    c=input()
    a=map(int,c.split())
    # if(c.isnumeric()):
    #     balls_list=sorted(balls_list)
    #     print(balls_list[min_ind]+k)
    #     min_ind+=1
    # else:
    #     a,b=map(int,c.split())
    
    print(f"a {a}")
    if(a==1):
        
        a,b=map(int,input().split())
        balls_list.append(b)
    elif(a==2):
        k+=b
    else:
        balls_list=sorted(balls_list)
        print(balls_list[min_ind]+k)
        min_ind+=1

        


