
for n in range(int(input())):
    h,v=map(int,input().split())
    if(h==v):
        print(2*h+2)
        # *-*-*-*-
        for i in range(2*h+2):
            if(i%2==0):
                print("1",end="")
            else:
                print("0",end="")
        print("")
    elif (h-v==1):
        print(2*h+1)
        for i in range(2*h+1):
            if(i%2==0):
                print("0",end="")
            else:
                print("1",end="")
        print("")
    elif (v-h==1):
        print(2*v+1)
        for i in range(2*v+1):
            if(i%2==0):
                print("1",end="")
            else:
                print("0",end="")
        print("")
    elif v>h:
        # v=4 h=1  10101101101
        
        print((2*(h+1)+(3*(v-h-1)))+1)
        for i in range(h+1):
            print("10",end="")
        for i in range(v-h-1):
            print("110",end="")
        print("1")
    elif h>v:
        print((2*(v+1)+(3*(h-v-1)))+1)
        for i in range(v+1):
            print("01",end="")
        for i in range(h-v-1):
            print("001",end="")
        print("0")

