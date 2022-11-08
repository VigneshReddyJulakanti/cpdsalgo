for i in range(int(input())):
    a=input().split()
    n=int(a[0])
    d=int(a[1])
    c=int(a[2])
    m=int(a[3])
    b=input()
    k=n
    ii=0
    while((d>0 or c>0 )and ii<n):
        if(b[ii]=="D"):
            if(d<1):
                break
            d-=1
            k-=1
            ii+=1
            c=c+m
        else:
            if(c<1):
                break
            c-=1
            k-=1
            ii+=1
    # print(f"The value of k is {k}")
    

    if(k==0):
        print(f"Case #{i+1}: YES")
    else:
        if("D" not in b[ii:]):
            print(f"Case #{i+1}: YES")
        else:
            print(f"Case #{i+1}: NO")
        