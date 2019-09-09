cipher_text = raw_input('Please key in the encoded message here in numbers form: ')
input_list = cipher_text.split()
input_list = [int(a) for a in input_list]

#print input_list

p_1 = input('Please key in your first password: ')
p_2 = input('Please key in your second password: ')
N = input('please enter your Public Key number: ')
e = input('please enter your Private Key number: ')

from fractions import gcd
from random import randint

invalid = True

def is_private_key(d):
    if gcd(e * d - 1, (p_1 - 1)*(p_2 - 1)) == (p_1 - 1)*(p_2 - 1):
        return True
    else:
        return False

while invalid:
    key = randint(0, N)
    if is_private_key(key) == True:
        invalid = False
    else:
        pass

#print key

def decrypt_1(input1):
    M = []
    for C in input1:
        M.append((C**key) % N)
    return M

list_number = decrypt_1(input_list)

#print list_number

def decrypt_2(input2):
    N = []
    for C in input2:
        N.append(chr(C))
    return N

final = ''.join(decrypt_2(list_number))

print
print 'Decrypted message: %s' % (final)
print
print 'Thank you for trusting our service!'
