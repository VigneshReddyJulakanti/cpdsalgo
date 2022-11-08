li=list(input().split())
temp=li[0]
temp=list(set(temp))
temp.sort()
ans=1
for i in li:
    temp1=i
    temp1=list(set(temp1))
    temp1.sort()
    if(temp1!=temp):
        ans=0
if(ans==1):
    print(True)
else:
    print(False)



