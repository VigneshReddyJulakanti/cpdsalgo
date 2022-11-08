for i in range(int(input())):
    a=input()
    b=input()
    k=0
    p=len(a)
    for j in a:
        l=b[k]
        if(j=="?" or l=="?"):
            
            if(k==p-1):
                print("Yes")
            
                break
            k+=1
            continue
        if(l!=j):
            print("No")
            break
        elif(k==p-1):
            print("Yes")
            break
        k+=1