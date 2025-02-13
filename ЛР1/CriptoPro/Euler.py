import time
import random
import math

# Функция для нахождения функции Эйлера по определению
def euler_lob(n):
    count = 0
    for i in range(1, n + 1):
        if math.gcd(n, i) == 1:
            count += 1

    print("Если всё перебирать: ", count)
    return count

def euler_formula(n):
    result = n
    prime_factors = set() # список простых множителей числа n
    i = 2
    while i * i <= n:
        while n % i == 0:
            prime_factors.add(i)
            n //= i
        i += 1

    if n > 1:
        prime_factors.add(n)

    for p in prime_factors:
        result *= (1 - 1 / p) # Формула m * p|m * (1 - 1/p)
    print("Если по формуле считать: ", round(result))
    return result


euler_lob(6)
euler_formula(6)