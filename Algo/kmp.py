txt="ababcdfgabababcd"
pat="abab"
n=len(txt)
m=len(pat)
lps=[0]*m
def kmp():
    j=0
    for i in range(n):
        if txt[i]==pat[j]:
            j+=1
            if j==m:
                print("Matched",i-j+1)
                j=lps[j-1]
        else:
            if j>1:
                j=lps[j-1]
                i=i-1
            

def computelps():
    i=1
    l=0
    while(i<m):
        # print("running",lps,i,l)
        if pat[i]==pat[l]:
            # print("equaled")
            l+=1
            # print(l,"l")
            lps[i]=l
            i+=1
        else:
            if l==0:
                i+=1
            else:
                l=lps[i-1]
computelps()
kmp()
# print(lps)





