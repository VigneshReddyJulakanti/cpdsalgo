nTestCases=int(input())
def funGolf():
    l=input().split()
    n=int(l[0])
    x=int(l[1])
    k=int(l[2])
    run=True
    
    if x%k==0 or (n-x-1)%k==0:
            print("yes")
    else:
            print("no")
for i in range(nTestCases): funGolf()