def is_prime(num):
    if num > 1:
        for i in range(2, num):
            if num % i == 0:
                return False
        return True


def get_primes(numbers):
    for el in [num for num in numbers]:
        if is_prime(el):
            yield el