'''
Find the min difference between two numbers in two arrays
https://atcoder.jp/contests/abc212/tasks/abc212_c
'''
n,m=map(int,input().split())
a=sorted(list(map(int,input().split())))
b=sorted(list(map(int,input().split())))

na=0
nb=0
min=abs(a[0]-b[0])
while(na<n and nb<m):
    k=abs(a[na]-b[nb])
    # print(f"k {k} = {a[na]} - {b[nb]}")
    if k<min:
        min=k
    if a[na]>=b[nb]:
        nb+=1
    else:
        na+=1


print(min)
