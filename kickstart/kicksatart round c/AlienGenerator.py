
for t in range(int(input())):
    g=int(input())
    n=1
    ans=0

    while n*(n-1)<2*g:
        if((g-(n*(n-1))/2)%n==0):
            ans+=1
        n+=1
    print(f"Case #{t+1}: {ans}")





























# for t in range(int(input())):
#     g=int(input())
#     ans=1
#     for k in range(1,int((2*g)**0.5)+1):
#         n=-((2*k)-1)+((((2*k)-1)**2)+(8*g))**0.5
#         if n.is_integer():
#             ans+=1
#     print(f"Case #{t+1}: {ans}")




# for t in range(int(input())):
#     g=int(input())
#     ans=0
#     for n in range(1,g):
#         if(g%n==0)and (n%2==1) and ((g/n)!=((n-1)/2)):
#             ans+=1
        
        
       
#     print(f"Case #{t+1}: {ans}")







# def alien_generator():
#     G =int( input())

#     result, l = 0, 1
#     while (l+1)*l//2 <= G:
#         # let k = K-1 => k*l + (1+l)*l//2 = G
#         if (G-(l+1)*l//2)%l == 0:
#             result += 1  # k = (G-(1+l)*l//2)//l >= 0
#         l += 1
#     return result

# for case in range(int(input())):
#     print(f"Case #{case+1}: {alien_generator()}")












# for t in range(int(input())):
#     g=int(input())
#     g=2*g
#     ans=0
#     i=1
#     while i**2<=g:
        
#         if(g%i==0):
#             a=i
#             b=int(g/i)

#             if ((a%2)^(b%2))==0:
#                 i+=1
#                 continue
#             n1=(b+a-1)/2
#             n2=(b-a-1)/2

#             s1=(n1**2+n1)
#             s2=(n2**2+n2)

#             if(s1-s2==g):
#                 ans+=1
#                 i+=1
#         else:
#             i+=1
#     print(f"Case #{t+1}: {ans}")

            



