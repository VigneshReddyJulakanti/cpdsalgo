a,b=map(int, input().split())
if(a>0 and b==0):
  print("Gold")
elif(b>0 and a==0):
  print("Silver")
else:
  print("Alloy")

