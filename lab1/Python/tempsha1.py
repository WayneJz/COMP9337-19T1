import hashlib
import time


#initializing string
def run(name):
    with open(name) as f:
        #str = f.read()
        str = [line.decode('utf-8').strip() for line in f.readlines()]

    start = time.time()
    result = hashlib.sha1(str[0].encode())
    hex_time = time.time() - start
    # printing the equivalent hexadecimal value.
    print("The hexadecimal equivalent of SHA1 is : ")
    print(result.hexdigest())
    return hex_time

if __name__ ==  '__main__':
    time = run('test2.txt')
    print(time)