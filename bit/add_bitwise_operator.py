# add 


def add_bitwise_operator(x,y):
    while y:
        carry = x & y
        x = x ^ y
	y = carry << 1
    return x




if __name__=='__main__':
    x = 3
    y = 2
    print add_bitwise_operator(x,y)
