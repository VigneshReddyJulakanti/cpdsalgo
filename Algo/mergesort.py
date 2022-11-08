def merge(arr,l,r,m):
    n1=m-l+1
    n2=r-m
    i=0
    j=0
    a=arr[l:m+1]
    b=arr[m+1:r+1]
    k=l
    while(i<n1 and j<n2):
        if a[i]<b[j]:
            arr[k]=a[i]
            i+=1
        else:
            arr[k]=b[j]
            j+=1
        k+=1
    while(i<n1):
        arr[k]=a[i]
        i+=1
        k+=1
    while(j<n2):
        arr[k]=b[j]
        k+=1
        j+=1
    

        
def mergesort(arr,l,r):
    if l<r:
        m=(l+r)//2
        mergesort(arr,l,m)
        mergesort(arr,m+1,r)
        merge(arr,l,r,m)
a=[4,1,3,2,10,8]
mergesort(a,0,len(a)-1)
print(a)


