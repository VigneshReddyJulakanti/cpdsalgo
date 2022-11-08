n=int(input())
list=[]
list_prime=[]
for i in range(n):
    a,b=map(int ,input().split())
    s=a+b
    list.append(s)
m=max(list)
n=0
i=2
while True:
    p=1
    for j in range(2,i):
        if(i%j==0):
            p=0
            break
    if p==1:
        list_prime.append(i)
        if(i>m):
            n=1
    i+=1
    if(n==1):
        break
for u in list:
    for k in list_prime:
        if k>u:
            print(k-u)
            break
    



    


    
        