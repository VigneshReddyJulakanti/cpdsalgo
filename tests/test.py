lix=[]
liy=[]
for i in range(int(input())):
    
    a,b=map(int,input().split())
    
    lix.append(a)
    liy.append(b)
lix=set(lix)
lix=list(lix)
lix=sorted(lix)
liy=set(liy)
liy=list(liy)
liy=sorted(liy)
# print(lix)
# print(liy)
lians=[abs(lix[-1]-lix[1]),abs(liy[-1]-liy[1]),abs(lix[-1]-lix[0]),abs(liy[-1]-liy[0])]

lians=sorted(lians)

print(lians[-2])

