
from Crypto.Cipher import AES
import  binascii


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

    cbc_key = binascii.unhexlify(key)
    iv = binascii.unhexlify(iv)

    cipher = AES_CBC_enc(cbc_key, iv, test_file)
    with open(outputfile, mode='ab') as file1:
        file1.write(cipher)

    decipher = AES_CBC_dec(cbc_key, iv, cipher)
    with open('deciper_file.txt', mode='ab') as file:
        file.write(decipher)


if __name__ == '__main__':
    '''''''''
    iv,key,inputfile,outputfile = [sys.argv[1],sys.argv[2],sys.argv[3],sys.argv[4]]

    '''''''''
    key = '40fedf386da13d57'
    iv = 'fedcba9876543210'

    run(iv, key, 'test.txt', 'tes.des')

