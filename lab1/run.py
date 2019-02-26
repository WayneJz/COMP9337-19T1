import time
import string
import random

# from tempaes import *
# from tempdes import *
# from tempHMAC import *
# from temprsa import *
# from tempsha1 import *


generator = {'DES': [8, 64, 512, 4096, 32768, 262144, 2047152],
            'AES': [8, 64, 512, 4096, 32768, 262144, 2047152],
            'HMACs': [8, 64, 512, 4096, 32768, 262144, 2047152],
            'SHA-1': [8, 64, 512, 4096, 32768, 262144, 2047152],
            'RSA': [2, 4, 8, 16, 32, 64, 128]}


def file_generator(type, size):
    file_name = type + '_' + str(size) + '.txt'
    with open(file_name, 'w') as file:
        for _ in range(0, size):
            file.write(random.choice(string.printable))



if __name__ == "__main__":
    file_generator('AES', 256)