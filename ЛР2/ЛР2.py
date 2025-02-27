import math

# Функция для вычисления символа Лежандра (a|p)

def legendre_symbol(a, p):
    ls = pow(a, (p - 1) // 2, p)
    print(f"Вычисляем символ Лежандра: ({a}|{p}) = {ls}")
    if ls == p - 1:
        return -1
    return ls


# Функция для решения квадратичного сравнения x^2 = a mod m
def solve_quadratic_congruence(a, m):
    print(f"Решаем квадратичное сравнение: x^2 ≡ {a} mod {m}")

    if m <= 1:
        return "Модуль m должен быть больше 1"

    # Проверяем, что 'a' и 'm' взаимно просты
    gcd_am = math.gcd(a, m)
    print(f"Находим НОД({a}, {m}) = {gcd_am}")
    if gcd_am != 1:
        return "a и m не взаимно просты. Решение может не существовать"

    # Проверяем, существует ли решение
    ls = legendre_symbol(a, m)
    if ls != 1:
        return "Решения не существует"

    # Находим все решения
    solutions = []
    print("Поиск решений:")
    for x in range(m):
        print(f"Проверяем x = {x}: {x}^2 mod {m} = {(x * x) % m}")
        if (x * x) % m == a % m:
            solutions.append(x)
            print(f"Найдено решение: x = {x}")

    if not solutions:
        return "Решения не найдены"

    return f"Решения: {solutions}, Количество решений: {len(solutions)}"


# Пример использования
a = 8
m = 17
result = solve_quadratic_congruence(a, m)
print(result)