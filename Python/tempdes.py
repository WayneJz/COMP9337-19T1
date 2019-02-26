#encoding=utf-8
from Crypto.Cipher import DES
from Crypto import Random
import sys
import binascii

def read_file(name):
    lis_pool = []
    patch = '0'
    global  blocksize
    with open(name) as f:
        a =  f.read()

    if a:
        for i in range(0, len(a), blocksize):
            if i + blocksize < len(a):
                lis_pool.append(a[i:i + blocksize])
            else:
                b = a[i:] + patch * (8 - len(a[i:]))

                lis_pool.append(b)


    return lis_pool


def DES_CBC_enc(cbc_key,iv,plain_text):
    des1 = DES.new(cbc_key, DES.MODE_CBC, iv)
    cipher_text = des1.encrypt(plain_text)
    return cipher_text



def  DES_CBC_dec(cbc_key,iv,cipher_text):
    des2 = DES.new(cbc_key, DES.MODE_CBC, iv)
    msg_text = des2.decrypt(cipher_text)
    return msg_text




if __name__ == '__main__':
    '''''''''
    iv,key,inputfile,outputfile = [sys.argv[1],sys.argv[2],sys.argv[3],sys.argv[4]]
    
    '''''''''
    blocksize = 8
    cbc_key = "\x40\xfe\xdf\x38\x6d\xa1\x3d\x57"


    test_file  = read_file("test2.txt")
    print(test_file)


    for i in test_file:
        iv = '\xfe\xdc\xba\x98\x76\x54\x32\x10'
        cipher = DES_CBC_enc(cbc_key,iv,i)
        print(cipher)
        decipher = DES_CBC_dec(cbc_key,iv,cipher)
        with open('dec_file.txt',mode='wa') as file:
                file.write(decipher)
        file.close()




