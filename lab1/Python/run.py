import time
import string
import random
import matplotlib.pyplot as plot

# from tempaes import *
from tempdes import run as desrun
# from tempHMAC import *
# from temprsa import *
# from tempsha1 import *


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
                        'HMACs': [[8, 0, 0], [64, 0, 0], [512, 0, 0], [4096, 0, 0], [32768, 0, 0], [262144, 0, 0], [2047152, 0, 0]],
                        'SHA-1': [[8, 0, 0], [64, 0, 0], [512, 0, 0], [4096, 0, 0], [32768, 0, 0], [262144, 0, 0], [2047152, 0, 0]],
                        'RSA': [[2, 0, 0], [4, 0, 0], [8, 0, 0], [16, 0, 0], [32, 0, 0], [64, 0, 0], [128, 0, 0]]}
        self.time = None

    def generator(self):
        for type in self.type_size.keys():
            for size in self.type_size[type]:
                self.file_generator(type, size[0])


    def file_generator(self, type, size):
        file_name = type + '_' + str(size) + '.txt'
        with open(file_name, 'w') as file:
            for _ in range(0, size):
                file.write(random.choice(string.printable))

    def function_call(self):
        for file in self.type_size['DES']:
            self.timer('Start')
            desrun(IV, KEY, 'DES' + '_' + str(file[0]) + '.txt', 'DESOUT' + '_' + str(file[0]) + '.txt')
            file[1] = self.timer()

    def timer(self, flag='Stop'):
        if flag == 'Start':
            self.time = time.time()
        else:
            return time.time() - self.time

    def visualization(self):
        for type in self.type_size.keys():
            plot.bar(range(len(self.type_size[type])), [x[1] for x in self.type_size[type]], 
            tick_label=[y[0] for y in self.type_size[type]], color='rgb')
            plot.title(type + ' Encryption')
            plot.xlabel('File Size')
            plot.ylabel('Time Consumed')
            plot.show()

            plot.bar(range(len(self.type_size[type])), [x[2] for x in self.type_size[type]], 
            tick_label=[y[0] for y in self.type_size[type]], color='rgb')
            plot.title(type + ' Decryption')
            plot.xlabel('File Size')
            plot.ylabel('Time Consumed')
            plot.show()


if __name__ == "__main__":
    testrun = Testrun()
    testrun.generator()
    testrun.function_call()
    testrun.visualization()