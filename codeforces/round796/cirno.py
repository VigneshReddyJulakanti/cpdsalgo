for _ in range(int(input())):
    n=int(input())
    i=1
    while True:
        if i!=n and i&n>0 and i^n>0:
            print(i)
            break
        i+=1