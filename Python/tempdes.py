#encoding=utf-8
from Crypto.Cipher import DES
import binascii

def read_file(name):
    patch = '\x00'
    blocksize = 8
    with open(name) as f:
        a =  f.read()

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

    cipher = DES_CBC_enc(cbc_key, iv, test_file)
    with open(outputfile, mode='a') as file1:
        file1.write(cipher)

    decipher = DES_CBC_dec(cbc_key, iv, cipher)
    with open('deciper_file.txt', mode='a') as file:
        file.write(decipher)




if __name__ == '__main__':

    '''''''''
    iv,key,inputfile,outputfile = [sys.argv[1],sys.argv[2],sys.argv[3],sys.argv[4]]
    
    '''''''''
    key = '40fedf386da13d57'
    iv = 'fedcba9876543210'
    run(iv, key, 'test.txt','tes.des')







