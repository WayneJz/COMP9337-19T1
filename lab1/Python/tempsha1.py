import hashlib
import time
import sys


#initializing string
def run(name):
    try:
        with open(name, encoding='utf-8') as f:
            str = [line.strip() for line in f.readlines()]
    except TypeError:       # for Python 2.7
        with open(name) as f:
            str = [line.decode('utf-8').strip() for line in f.readlines()]

    start = time.time()
    result = hashlib.sha1(str[0].encode())
    hex_time = time.time() - start
    # printing the equivalent hexadecimal value.
    print("The hexadecimal equivalent of SHA1 is : ")
    print(result.hexdigest())
    return hex_time

if __name__ ==  '__main__':

    inputfile = sys.argv[1]
    time = run(inputfile)
    print('hash time : ',time)