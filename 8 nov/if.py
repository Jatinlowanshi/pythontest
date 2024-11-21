#write a program to calculate 

n=str(input("enter a character"))
vowel_str="aAeEiIoOuU"
consonent_str="bBcCdDfFgGhHjJkKlLmMnNPpqQrRSstTvVwWxXyYzZ"
if n in vowel_str:
 print("charater is voule")
elif n in consonent_str:
 print("charater is consonent")
else:
 print("invelid")