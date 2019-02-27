#Following code reads its source file and computes an HMAC signature for it:
import hmac
import time

def run(name):

    digest_maker = hmac.new('secret-shared-key-goes-here')

    f = open(name, 'rb')
    try:
        while True:
            block = f.read()
            if not block:
                break
            digest_maker.update(block)
    finally:
        f.close()
    start = time.time()
    digest = digest_maker.hexdigest()
    digest_time = time.time() - start
    print (digest)
    return  digest_time


if __name__ =='__main__':
    time = run('test2.txt')
    print(time)

