import hashlib


#initializing string
def run(name):
    with open(name) as f:
        str = f.read()

    result = hashlib.sha1(str.encode())
    # printing the equivalent hexadecimal value.
    print("The hexadecimal equivalent of SHA1 is : ")
    print(result.hexdigest())


run('test2.txt')