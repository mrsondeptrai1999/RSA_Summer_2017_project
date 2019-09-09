from random import randint
from fractions import gcd

def isPrime(p):
    if(p==2): return True
    if(not(p&1)): return False
    return pow(2,p-1,p)==1

invalid = True

while invalid:
   n = randint(10,100)
   if isPrime(n) == True:
       invalid = False
   else:
       pass


invalid = True

while invalid:
   m = randint(10,100)
   if isPrime(m) == True: 
       invalid = False
   else:
       pass

invalid = True

while invalid:
   e = randint(10,100)
   if isPrime(e) == True: 
       invalid = False
   else:
       pass
       
N = m * n


if gcd(e, (m-1)*(n-1)) == 1 and m != n != e:
    print 'Here is your first password: %s' % (m)
    print 'Here is your second password: %s' % (n)
    print 'Here is your Public Key number: %s' % (N)
    print 'Here is your Private Key number: %s' % (e)
else:
    print 'Sorry! You have encountered an extremely rare case of failure. Please retry!'

