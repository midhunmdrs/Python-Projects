# from functools import reduce
from functools import reduce


def is_even(n):
    return n % 2 == 0


def is_double(n):
    return n * 2


def add_all(a,b):
    return a + b


nums = [2, 4, 3, 7, 8, 11, 13, 15]

evens = list(filter(is_even, nums))
evens2 = list(filter(lambda l: l % 2 == 0, nums))

update = list(map(is_double, evens))
update1 = list(map(lambda n: n * 2, evens))

sums = reduce(add_all,update)
sums2 = reduce(lambda a,b : a+b ,nums)

print(evens)
print(evens2)

print(update)
print(update1)

print(sums)
print(sums2)
