#1
from inspect import isgenerator
def pow(x):
    return x ** 2

def some_gen(begin, end, func):
    current_value = begin
    for i in range(end):
        yield current_value
        current_value = func(current_value)

gen = some_gen(2, 4, pow)


assert isgenerator(gen) == True, 'Test1'
assert list(gen) == [2, 4, 16, 256], 'Test2'
print('OK')



#2

def is_even(digit):
    return digit % 2 == 0


assert is_even(2) == True, 'Test1'
assert is_even(5) == False, 'Test2'
assert is_even(0) == True, 'Test3'
print('OK')











