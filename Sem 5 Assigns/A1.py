'''
Assignmrnt 1
Implement Euclid’s algorithm to find the GCD of two integers. Further implement
extended Euclidean algorithm to find the multiplicative inverse of the given integer.
'''
import math

# GCD Euclids Algorithm
def gcd(m,n):
    if m<n: # Assume m>=n
        (m,n)=(n,m)
    while(m%n) != 0:
        (m,n) = (n,m%n) # m%n < n, always!
    return(n)

print("GCD is",gcd(16,12))


# GCD Extended Euclids Algorithm
def xgcd(a, b, s1 = 1, s2 = 0, t1 = 0, t2 = 1):
   
   if(b == 0):
      return abs(a), 1, 0
   
   q = math.floor(a/b)
   r = a - q * b
   s3 = s1 - q * s2
   t3 = t1 - q * t2
   
   #if r==0, then b will be the gcd and s2, t2 the Bezout coefficients
   return (abs(b), s2, t2) if (r == 0) else xgcd(b, r, s2, s3, t2, t3)


  
# Multiplicative Inverse using Extended Euclids Algorithm
def multinv(b, n):
    
    #Get the gcd and the second Bezout coefficient (t)
    #from the Extended Euclidean Algorithm. (We don't need s)
    my_gcd, _, t = xgcd(n, b)

    #It only has a multiplicative inverse if the gcd is 1
    if(my_gcd == 1):
       return t % n
    else:
       raise ValueError('{} has no multiplicative inverse modulo {}'.format(b, n))
xgcd(10,5)
print(multinv(5,4))





