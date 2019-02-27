
from Crypto.Cipher import AES
import time
from Crypto import Random


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


def AES_CBC_enc(cbc_key, iv, plain_text):
    aes1 = AES.new(cbc_key, AES.MODE_CBC, iv)
    cipher_text = aes1.encrypt(plain_text)
    return cipher_text


def AES_CBC_dec(cbc_key, iv, cipher_text):
    aes2 = AES.new(cbc_key, AES.MODE_CBC, iv)
    msg_text = aes2.decrypt(cipher_text)
    return msg_text


def run(iv, key, inputfile, outputfile):
    test_file = read_file(inputfile)

    start1 = time.time()
    cipher = AES_CBC_enc(key, iv, test_file)
    cipher_time = time.time() - start1


    with open(outputfile, mode='wb') as file1:
        file1.write(cipher)


    start2 = time.time()
    decipher = AES_CBC_dec(key, iv, cipher)
    decipher_time =time.time() -  start2


    with open('deciper_file.txt', mode='wb') as file:
        file.write(decipher)

    return cipher_time,decipher_time


if __name__ == '__main__':
    '''''''''
    iv,key,inputfile,outputfile = [sys.argv[1],sys.argv[2],sys.argv[3],sys.argv[4]]

    '''''''''
    cbc_key = Random.get_random_bytes(16)
    iv = Random.get_random_bytes(16)

    a,b = run(iv, cbc_key, 'test.txt', 'tes.des')
    print(a)
    print(b)

