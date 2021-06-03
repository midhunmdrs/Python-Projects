def sub(a, b):  # actual function definition
    print(a - b)


def smart_sub(func):  # func is replaced by inner_func

    def inner_func(a, b):  # inner func executed first
        if a < b:  # check condition if true swap a,b
            a, b = b, a
        return func(a, b)  # return swaped a,b to inner_func

    return inner_func


sub = smart_sub(sub)  # actual function sub is called here as sub1
sub(3, 4)
