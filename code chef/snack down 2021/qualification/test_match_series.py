for n in range(int(input())):
    a=input().split()
    ind=0
    eng=0
    for i in a:
        if i=="1":
            ind+=1
        elif i=="2":
            eng+=1
    if ind>eng:
        print("INDIA")
    elif ind==eng:
        print("DRAW")
    else:
        print("ENGLAND")