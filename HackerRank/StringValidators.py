import re
s = input()

print(any(i.isalnum() for i in s))
print(any(i.isalpha() for i in s))#Contains any characters
print(any(i.isdigit() for i in s))#Contains any digits
print(any(i.islower() for i in s))#Contains any a-z characters
print(any(i.isupper() for i in s))#Contains any A-Z characters

