import Crypto
from Crypto.PublicKey import RSA
from Crypto import Random
import ast

def read_file(name):
    patch = '\x00'
    blocksize = 8
    with open(name) as f:
        a = f.read()

    if a:
        for i in range(0, len(a), blocksize):
            if i + blocksize < len(a):
                pass
            else:
                patch_num = 8 - len(a[i:])
                b = a + patch * (patch_num)

    return b



#with open('test2.txt') as f1:
    #a = f1.read()

a= read_file('test2.txt')
random_generator = Random.new().read
key = RSA.generate(1024, random_generator) #generate pub and priv key

publickey = key.publickey() # pub key export for exchange

encrypted = publickey.encrypt(a,32)
#message to encrypt is in the above line 'encrypt this message'
print ('encrypted message:', encrypted) #ciphertext

#decrypted code below
decrypted = key.decrypt(ast.literal_eval(str(encrypted)))
print ('decrypted', decrypted)



