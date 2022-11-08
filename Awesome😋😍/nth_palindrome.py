'''
Find the nth palindrome
'''

a=input()
d=len(a)
k=d//2+d%2
j=int("1"+((k-1)*"0"))

def pref(n):
    if(n==0):
        return 0
    if(len(str(n))%2==0):
        return int("9"+(((len(str(n)))*"0"))  )
    else:
        return int("9"+(((len(str(n))-1)*"0"))  )



m=int(a)
