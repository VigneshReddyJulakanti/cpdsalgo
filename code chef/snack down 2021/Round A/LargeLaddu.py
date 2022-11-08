def ans():
    b=int(input())

    
    li=input().split()
    if(b==0):
        print("YES")
        return
    li=set(li)
    li=list(li)
    if(len(li)==1):
        print("YES")
        return

    if(len(li)==2):
        if(abs(int(li[0])-int(li[1]))<2):
            print("YES")
        else:
            print("NO")
    else:
        print("NO")

for n in range(int(input())):
    ans()




