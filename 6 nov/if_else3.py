n=int(input("enter the no"))

d1=n//100
d2=n//10%10
d3=n%10
res=d1**3+d2**3+d3**3

if res==n:
 print("no is amstrong")
else:
 print("no is not amstrong")