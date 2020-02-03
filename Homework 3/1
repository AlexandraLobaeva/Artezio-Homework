import math
# 1. 3 functions


def square_return(*args):
    sqr = []
    for el in args:
        sqr.append(el * el)
    return sqr


print(square_return(1, 2, 3, 4, 5))


def even_numb_return(*args):
    even_numb_list = []
    for el in range(1, len(args)):
        if el % 2 == 0:
            even_numb_list.append(el)
    return even_numb_list


print(even_numb_return(1, 2, 3, 4, 5))


def odd_cube(*args):
    odd_cube_list = []
    for el in range(1, len(args)+1):
        if el % 2 != 0:
            odd_cube_list.append(int(math.pow(el, 3)))
    return odd_cube_list


print(odd_cube(1, 2, 3, 4, 5))
