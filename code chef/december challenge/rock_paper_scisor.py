def hlo(a,b):
    if(a=="R" and b=="S") or ( b=="R" and a=="S"):
        return "R"
    elif(a=="R" and b=="P") or (b=="R" and a=="P"):
        return "P"
    elif(a=="P" and b=="S") or (b=="P" and a=="S"):
        return "S"
for n in range(int(input())):
    a=int(input())
    b=input()
    mans=""
    for i in range(len(b)-1):
        
        t=b[i]
        for j in range(i+1,len(b)-1):
            # print("i",i)
            t=hlo(t,b[j+1])
        mans+=t
    mans+=b[-1]
    print(mans)
        


    