import random
import string

print("Welcome to Random Password Generator")
length=int(input("Enter the length of password you want: "))
lowerData=string.ascii_lowercase
upperData=string.ascii_uppercase
digitData=string.digits
symbolData=string.punctuation
combine=lowerData+upperData+digitData+symbolData
x=random.sample(combine,length)
password="".join(x)
print("Your password is:",password)