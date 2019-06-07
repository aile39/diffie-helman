import random

p = 65537
g = 29


def PablicKey(Private_number):
    Public_key = g ** Private_number % p
    return Public_key

def PrivateKey(Public_key,Private_number):
    Private_Key = Public_key ** Private_number % p
    return Private_Key

# Alice makes public key

a = random.randint(1, p - 2)
A = PablicKey(a)

# Bob makes public key

b = random.randint(1, p - 2)
B = PablicKey(b)

# Alice makes private key

C = PrivateKey(B,a)
print(C)

# Bob makes private key

D = PrivateKey(A, b)
print(D)