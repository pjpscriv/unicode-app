#!/usr/bin/env python
from time import sleep


def main():

    print(" -- Test Range! --")

    for i in range(100):
        thing = chr(i)
        
        print("{:2}: ".format(i), end="")
        try:
            info(thing)
        except UnicodeEncodeError as err:
            print(err)
            sleep(0.001)
        #sleep(0.00001)

    print()

    info("hello")

    bb = b'\x80abc'

    print(bb)





    print("Done!")

def info(string1):
    enc_bytes = string1.encode('utf-8')
    s_len = len(string1)

    # if len(v1) > 1:
    #     for b in v1:
    #         info(b)
            
    b_len = len(enc_bytes)
    # thing = i
    #number = bin(number[0])

    # Graphemes
    print("\"{0:}\", {1:2},  ".format(string1, s_len,), end="")
    if (s_len < 1):
        input("Wow!")
    # Numbers
    print("utf8 : {},   {}".format(enc_bytes, b_len))
    # Bytes


def bits():
    print(chr(42))
    bb = bin(42)[2:]
    bb = "{:0>8}".format(bb)
    bb = bb[:4] + chr(8201) + bb[4:]
    print(bb)
    print(type(bb))
    for b in bb:
        print(b)

# main()
# bits()

def bins():
    s  = "1001 0001"
    s2 = "0010 0011"
    print(type(bin(43)))

    d = s[:4] + s[5:]

    print(s, d)

    i = int(d, 2)

    print(i)

    b1 = b'\xff'
    b2 = b'\xfc'
    b3 = b'\xf1'

    print(type(b1))

    print(b1+b2+b3)



bins()
