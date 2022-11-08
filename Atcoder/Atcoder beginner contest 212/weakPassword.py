
def check():
    a=input()
    if(a[0]==a[1]==a[2]==a[3]):
        return "Weak"
    for i in range(4):
        if(i==3):
            return "Weak"
        if(int(a[i])==9):
            if(int(a[i+1])==0):
                continue
            break
        if(1+int(a[i])==int(a[i+1])):
            continue

        return "Strong"
    return "Strong"
print(check())

        

