#write a program to calculate 

n=str(input("enter a character"))
upper_str="ABCDEFGHIJKLMNOPQSRTUVWXYZ"
lower_str="abcdefghijklmnopqrstuvwzxy"
if n in upper_str:
 print("charater is upper case")
elif n in lower_str:
 print("charater is lower case")
else:
 print("invelid")