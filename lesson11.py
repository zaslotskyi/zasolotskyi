from inspect import isgenerator

#1
def prime_generator(end):
    for num in range(2, end + 1):
        is_prime = True
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                is_prime = False
        if is_prime:
            yield num


gen = prime_generator(29)

assert isgenerator(gen) == True, 'Test0'
assert list(prime_generator(10)) == [2, 3, 5, 7], 'Test1'
assert list(prime_generator(15)) == [2, 3, 5, 7, 11, 13], 'Test2'
assert list(prime_generator(29)) == [2, 3, 5, 7, 11, 13, 17, 19, 23, 29], 'Test3'
print('Ok')




#2


def is_even(number):
    return not number & 1


# ну або якщо псіханути))))
def is_even(number):
    list_number = list(str(number))
    if (list_number[-1] == '0'
            or list_number[-1] == '2'
            or list_number[-1] == '4'
            or list_number[-1] == '6'
            or list_number[-1] == '8'):
        return True
    else:
        return False


assert is_even(2494563894038**2) == True, 'Test1'
assert is_even(1056897**2) == False, 'Test2'
assert is_even(24945638940387**3) == False, 'Test3'
print('Ok')




