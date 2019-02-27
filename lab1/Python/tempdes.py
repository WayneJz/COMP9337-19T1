#encoding=utf-8
from Crypto.Cipher import DES
import binascii
import time
import sys

def read_file(name):
    patch = '\x00'
    blocksize = 8
    with open(name) as f:
        a =  f.read()
        b = a

    if a:
        for i in range(0, len(a), blocksize):
            if i + blocksize < len(a):
                pass
            else:
                patch_num = 8 - len(a[i:])
                b = a + patch * (patch_num)

    return b

def DES_CBC_enc(cbc_key,iv,plain_text):
    des1 = DES.new(cbc_key, DES.MODE_CBC, iv)
    cipher_text = des1.encrypt(plain_text)
    return cipher_text



def  DES_CBC_dec(cbc_key,iv,cipher_text):
    des2 = DES.new(cbc_key, DES.MODE_CBC, iv)
    msg_text = des2.decrypt(cipher_text)
    return msg_text

def run(iv,key,inputfile, outputfile):
    test_file = read_file(inputfile)
    cbc_key = binascii.unhexlify(key)
    iv = binascii.unhexlify(iv)

    start1 = time.time()
    cipher = DES_CBC_enc(cbc_key, iv, test_file)
    cipher_time = time.time() - start1

    with open(outputfile, mode='wb') as file1:
        file1.write(cipher)

    start2 = time.time()
    decipher = DES_CBC_dec(cbc_key, iv, cipher)
    decipher_time = time.time() - start2

    with open('deciper_file.txt', mode='wb') as file:
        file.write(decipher)

    return cipher_time , decipher_time


if __name__ == '__main__':

    #key = '40fedf386da13d57'
    #iv = 'fedcba9876543210'

    iv,key,inputfile,outputfile = sys.argv[1],sys.argv[2],sys.argv[3],sys.argv[4]
    a,b = run(iv,key,inputfile,outputfile)
    print('encryption time : ',a)
    print('decryption time : ',b)







