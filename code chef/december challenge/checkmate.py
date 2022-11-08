import sys
input = sys.stdin.readline
for n in range(int(input())):
    kx,ky=map(int,input().split())
    h1x,h1y=map(int,input().split())
    h2x,h2y=map(int,input().split())
    i=1
    if(kx!=1 and ky!=1 and kx!=8 and ky!=8):
         print("NO")
         continue
    elif(kx==1 and ky==1) :
        i=0
        if(h1x-kx!=1 and h1y-ky!=1 and h2x-kx!=1 and h2y-ky!=1):               
              print("NO")
              continue
    elif (kx==8  and ky==8) :
        i=0
        if(h1x-kx!=-1 and h1y-ky!=-1 and h2x-kx!=-1 and h2y-ky!=-1):               
              print("NO")
              continue
    elif (kx==1  and ky==8) :
        i=0
        if(h1x-kx!=1 and h1y-ky!=-1 and h2x-kx!=1 and h2y-ky!=-1):               
              print("NO")
              continue
    elif (kx==8  and ky==1) :
        i=0
        if(h1x-kx!=-1 and h1y-ky!=1 and h2x-kx!=-1 and h2y-ky!=1):               
              print("NO")
              continue


    if(i!=0):
        if(kx==1 and abs(kx-h1x)!=1 and abs(kx-h2x)!=1):
            print("NO")
            continue
        elif(ky==1 and abs(ky-h1y)!=1 and abs(ky-h2y)!=1):
            print("NO")
            continue
        elif(kx==8 and abs(kx-h1x)!=1 and abs(kx-h2x)!=1):
            print("NO")
            continue
        elif(ky==8 and abs(ky-h1y)!=1 and abs(ky-h2y)!=1):
            print("NO")
            continue

        
        

    if(kx==h1x==h2x or ky==h2x==h1x):
        print("NO")
    elif(abs(ky-h2y)==1 and h2x==h1x):
        print("NO")
    elif(abs(kx-h1x)==1 and h2y==h1y):
        print("NO")
    elif(abs(ky-h1y)==1 and h2x==h1x):
        print("NO")
    elif(abs(kx-h2x)==1 and h2y==h1y):
        print("NO")
    elif(abs(kx-h1x)==1 and abs(ky-h2y)==1):
        print("NO")
    elif(abs(ky-h1y)==1 and abs(kx-h2x)==1):
        print("NO")
    else:
        print("YES")