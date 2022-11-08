    # import sys
    # sys.setrecursionlimit(10**5)
def powee(a,b,m=(10**9+7)):
        ans=1
        while(b>0):
            if(b&1):
                ans=(ans*a)%m
            a=(a*a)%m
            b=b>>1
        return ans
for i in range(int(input())):
        n,k=map(int , input().split())
        fn=n
        s=input()
        # a="abcdefghijklmnopqrstuvwxyz"
        inno=0
        subans=0
        def hlo(n,inno):
            if(n%2==0):
                
                        
                if(n==0): 
                    boom=int(fn/2)
                    for j in range(boom):
                        if (s[boom-j-1])<s[-(boom-j)]:
                            return 1
                        if (s[boom-j-1])>=s[-(boom-j)]:
                            return 0
                    return 0

                b=(ord(s[inno])-97)


                # if(n==0): 
                #     if(a.index(s[-(inno)])>a.index(s[-(inno+1)])):
                #         return 1
                #     else:
                #          return 0
                # if(b==0) and (inno==0):
                    # if(a.index(s[-(inno+1)])>b):
                        # return  hlo(n-2,inno+1)

                if(b==0) :
                    # if(a.index(s[-(inno+1)])>b):
                    #     return 1+ hlo(n-2,inno+1)
                    # else:
                        return hlo(n-2,inno+1)
                m=min(k,b)
                subans=(m)*(powee(k,int(n/2)-1))
                return (subans%((10**9)+7))+hlo(n-2,inno+1)
            else:
                if(n<=0): return 0
                b=ord(s[inno])-97
                        
                if(n==1): 
                    boom=int(fn/2)
                    for j in range(boom):
                        if (s[boom-j-1])<s[-(boom-j)]:
                            return min(k%((10**9)+7),((ord(s[inno])+1)-97)%((10**9)+7))
                        if (s[boom-j-1])>s[-(boom-j)]:
                            return min(k%((10**9)+7),((ord(s[inno])-97)%((10**9)+7)))


                    return min(k%((10**9)+7),((ord(s[inno])-97)%((10**9)+7)))
                # if(b==0) and (inno==0):
                #     if(a.index(s[-(inno+1)])>b):
                #         return 1+ hlo(n-2,inno+1)
                if(b==0) :
                    # if(a.index(s[-(inno+1)])>b):
                    #     return 1+ hlo(n-2,inno+1)
                    # else:
                        return hlo(n-2,inno+1)
                m=min(k,b)
                subans=(m)*(powee(k,int(n/2)))
                return (subans%((10**9)+7))+(hlo(n-2,inno+1)%((10**9)+7))



print(f"case #{i+1}: {(hlo(n,0))%((10**9)+7)}")
