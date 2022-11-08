


for n in range(int(input())):
    a=int(input())

    if(a%2==0):
        for i in range(a):
            for j in range(a):
                if(i==1):
                    print(".",end="")
                    continue
                if(i==a-1):
                    print(".",end="")
                    continue
                if(i==j):
                    print("Q",end="")
                else:
                    print(".",end="")
            print("")
    else:
        if(a==3):
            print("...")
            print(".Q.")
            print("...")
            continue
        for i in range(a):
            for j in range(a):
                if(i==0):
                    print(".",end="")
                    continue
                if(i==a-1):
                    print(".",end="")
                    continue
                if(i==j):
                    print("Q",end="")
                else:
                    print(".",end="")
            print("")

        


   
        