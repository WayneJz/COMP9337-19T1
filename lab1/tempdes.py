
from Crypto.Cipher import DES
from Crypto import Random
cbc_key = "\x01\x23\x45\x67\x89\xab\xcd\xef"
iv = Random.get_random_bytes(8)

des1 = DES.new(cbc_key, DES.MODE_CBC, iv)
des2 = DES.new(cbc_key, DES.MODE_CBC, iv)

plain_text = 'abcdefgh'
print(plain_text)

cipher_text = des1.encrypt(plain_text)
print(cipher_text)

msg=des2.decrypt(cipher_text)
print(msg)

