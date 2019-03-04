import time
import string
import random
import matplotlib.pyplot as plot

from tempaes import run as aesrun
from tempdes import run as desrun
from tempHMAC import run as HMACrun
from tempsha1 import run as sha1run
from temprsa import run as rsarun


KEY = '40fedf386da13d57'
IV = 'fedcba9876543210'

'''
    Structure Definition of self.type_size

    {Algorithm Name: [[File Size, Encryption Time, Decryption Time], ...], ...}
'''

class Testrun:
    def __init__(self):
        self.type_size = {'DES': [[8, 0, 0], [64, 0, 0], [512, 0, 0], [4096, 0, 0], [32768, 0, 0], [262144, 0, 0], [2047152, 0, 0]],
                        'AES': [[8, 0, 0], [64, 0, 0], [512, 0, 0], [4096, 0, 0], [32768, 0, 0], [262144, 0, 0], [2047152, 0, 0]],
                        'HMAC': [[8, 0, 0], [64, 0, 0], [512, 0, 0], [4096, 0, 0], [32768, 0, 0], [262144, 0, 0], [2047152, 0, 0]],
                        'SHA-1': [[8, 0, 0], [64, 0, 0], [512, 0, 0], [4096, 0, 0], [32768, 0, 0], [262144, 0, 0], [2047152, 0, 0]],
                        'RSA': [[2, 0, 0], [4, 0, 0], [8, 0, 0], [16, 0, 0], [32, 0, 0], [64, 0, 0], [128, 0, 0]]}
        self.time = None

    def generator(self):
        for type in self.type_size.keys():
            for size in self.type_size[type]:
                self.file_generator(type, size[0])


    def file_generator(self, type, size):
        file_name = type + '_' + str(size) + '.txt'
        print('Generating test file ' + file_name)
        with open(file_name, 'w') as file:
            for _ in range(0, size):
                file.write(random.choice(string.printable))

    def function_call(self):
        for des in self.type_size['DES']:
            des[1], des[2] = desrun(IV, KEY, 'DES' + '_' + str(des[0]) + '.txt', 'DES_OUT' + '_' + str(des[0]) + '.des')
        for aes in self.type_size['AES']:
            aes[1], aes[2] = aesrun('AES' + '_' + str(aes[0]) + '.txt', 'AES_OUT' + '_' + str(aes[0]) + '.aes')
        for HMAC in self.type_size['HMAC']:
            HMAC[1] = HMACrun('HMAC' + '_' + str(HMAC[0]) + '.txt')
        for sha1 in self.type_size['SHA-1']:
            sha1[1] = sha1run('SHA-1' + '_' + str(sha1[0]) + '.txt')
        for rsa in self.type_size['RSA']:
            rsa[1], rsa[2] = rsarun('RSA' + '_' + str(rsa[0]) + '.txt')
  

    def timer(self, flag='Stop'):
        if flag == 'Start':
            self.time = time.time()
        else:
            return time.time() - self.time

    def visualization(self):
        for type in self.type_size.keys():
            plot.bar(range(len(self.type_size[type])), [x[1] * 1000000 for x in self.type_size[type]],
            tick_label=[y[0] for y in self.type_size[type]], color='rgb')
            for a, b in enumerate([y[1] * 1000000 for y in self.type_size[type]]):
                plot.text(a, b + b * 0.01, '%.4f' %b, ha='center', va='bottom', fontsize=8)
            plot.title(type + ' Encryption')
            plot.xlabel('File Size (Bytes)')
            plot.ylabel('Time Consumed (Microseconds)')
            plot.savefig('./' + type + '_Encryption' + '.png')
            plot.show()

            if type in ['SHA-1', 'HMAC']:
                continue
            plot.bar(range(len(self.type_size[type])), [x[2] * 1000000 for x in self.type_size[type]],
            tick_label=[y[0] for y in self.type_size[type]], color='rgb')
            for a, b in enumerate([y[2]  * 1000000 for y in self.type_size[type]]):
                plot.text(a, b + b * 0.01, '%.4f' %b, ha='center', va='bottom', fontsize=8)
            plot.title(type + ' Decryption')
            plot.xlabel('File Size (Bytes)')
            plot.ylabel('Time Consumed (Microseconds)')
            plot.savefig('./' + type + '_Decryption' + '.png')
            plot.show()


if __name__ == "__main__":
    testrun = Testrun()
    testrun.generator()
    testrun.function_call()
    testrun.visualization()