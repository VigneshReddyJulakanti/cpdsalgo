import random
a=0
b=100
n = random.randint(a,b)
print(f"Enter a number between  {a} and {b}")
score=0
while(True):
    score+=1
    m=int(input())
    if(m==n):
        print(f"You won your score is{score}")
        break
    elif(m>n):
        print(f"the answer is less than {m} ")
    else:
        print(f"the answer is greater than {m}")