a="abh"
def rec(s,ind,n):
    if(len(s)>0):
        print(s)
    if(ind>=n):
        return
    rec(s+a[ind],ind+1,n)
    if(ind+1<n):
        rec(s,ind+1,n)
    


rec("",0,len(a))