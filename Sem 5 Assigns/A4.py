'''
Assignment 4:
Write a program to implement SHA1 algorithm using libraries (API)
'''

# Reference: https://www.geeksforgeeks.org/sha-in-python/


# Python 3 code to demonstrate
# SHA hash algorithms.

import hashlib

# initializing string
str = "Shreyash"

# encoding using encode()
# then sending to SHA1()
result = hashlib.sha1(str.encode())

# printing the equivalent hexadecimal value.
print("The hexadecimal equivalent of SHA1 is : ")
print(result.hexdigest())


