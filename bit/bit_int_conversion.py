# conversion between bit and int

from collections import deque

def int_to_bit_big_endian(num):
    bytestr = deque()
    while num > 0:
        bytestr.appendleft(num & 0xff)
        num >>= 8
    return bytes(bytestr)

def int_to_bit_small_endian(num):
    bytestr = list()
    while num > 0:
        bytestr.append(num & 0xff)
        num >>= 8
    return bytestr

def bit_big_endian_to_int(bytestr):
    num = 0
    for b in bytestr:
        num <<= 8
        num += b
    return num

def bit_small_endian_to_int(bytestr):
    num = 0
    e = 0
    for b in bytestr:
        num += b << e
        e += 8
    return num


if __name__=='__main__':
    a = 255
    print bit_to_int_big_endian(a)
    b= 123141
    print bit_to_int_small_endian(b)
