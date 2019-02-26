import time
import string
import random
import matplotlib.pyplot as plot

# from tempaes import *
# from tempdes import *
# from tempHMAC import *
# from temprsa import *
# from tempsha1 import *

'''
    Structure Definition for self.type_size

    {Algorithm Name : [[File Size, Encryption Time, Decryption Time]...], ...}
'''

class Testrun:
    def __init__(self):
        self.type_size = {'DES': [[8, 0], [64, 0], [512, 0], [4096, 0], [32768, 0], [262144, 0], [2047152, 0]],
                        'AES': [[8, 0], [64, 0], [512, 0], [4096, 0], [32768, 0], [262144, 0], [2047152, 0]],
                        'HMACs': [[8, 0], [64, 0], [512, 0], [4096, 0], [32768, 0], [262144, 0], [2047152, 0]],
                        'SHA-1': [[8, 0], [64, 0], [512, 0], [4096, 0], [32768, 0], [262144, 0], [2047152, 0]],
                        'RSA': [[2, 0], [4, 0], [8, 0], [16, 0], [32, 0], [64, 0], [128, 0]]}
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
        pass

    def timer(self, flag='Stop'):
        if flag == 'Start':
            self.time = time.time()
        else:
            return time.time() - self.time

    def visualization(self):
        plot.bar(range(len(self.type_size['DES'])), [x[1] for x in self.type_size['DES']], 
        tick_label=[y[0] for y in self.type_size['DES']], color='rgb')
        plot.title('DES')
        plot.xlabel('File Size')
        plot.ylabel('Time Consumed')
        plot.show()

if __name__ == "__main__":
    testrun = Testrun()
    testrun.visualization()