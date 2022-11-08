def powee(a,b,m=(10**7+7)):
    ans=1
    while(b>0):
        if(b&1):
            ans=(ans*a)%m
        a=(a*a)%m
        b=b>>1
    return ans
print(powee(247726,532728))