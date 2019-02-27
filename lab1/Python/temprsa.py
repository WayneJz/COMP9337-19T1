import Crypto
from Crypto.PublicKey import RSA
from Crypto import Random
import ast
import time
import sys


def read_file(name):
    patch = '\x00'
    blocksize = 8
    with open(name) as f:
        a = f.read()
        b = a

    if a:
        for i in range(0, len(a), blocksize):
            if i + blocksize < len(a):
                pass
            else:
                patch_num = 8 - len(a[i:])
                b = a + patch * (patch_num)

    return b


def run(name):
    file = read_file(name)
    random_generator = Random.new().read
    key = RSA.generate(1024, random_generator) #generate pub and priv key

    publickey = key.publickey() # pub key export for exchange

    start1 = time.time()
    try:    # for Python 2.7 and Python 3.6, different positions of arguments 
        encrypted = publickey.encrypt(file,32)
    except TypeError:
        encrypted = publickey.encrypt(32,file)

    cipher_time = time.time() - start1

    #message to encrypt is in the above line 'encrypt this message'
    print('encrypted message:', encrypted) #ciphertext

    #decrypted code below
    start2 = time.time()
    decrypted = key.decrypt(ast.literal_eval(str(encrypted)))
    decipher_time = time.time() - start2
    print('decrypted', decrypted)

    return cipher_time , decipher_time



if __name__ == "__main__":

    inputfile = sys.argv[1]
    a,b = run(inputfile)
    print('encryption time : ',a)
    print('decryption time : ',b)


