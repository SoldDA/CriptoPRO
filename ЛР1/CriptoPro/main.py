from math import gcd

def extended_gcd(a, b):
    # Алгоритм Евклида, возвращает НОД(a, b), x, y такие что ax + by = НОД(a, b)
    if a == 0:
        return b, 0, 1
    gcd_val, x1, y1 = extended_gcd(b % a, a)

    # Вывод текущих шагов
    print(f"Вычисляем: {a} * {x1} + {b} * {y1} = {gcd_val}")

    x = y1 - (b // a) * x1
    y = x1
    return gcd_val, x, y

def solve_congruences_extended(a, b, m):
    # Решение сравнения ax ≡ b mod m
    gcd_ab_m = gcd(a, m)

    print(f"НОД({a}, {m}) = {gcd_ab_m}")

    # Если b не кратно НОД(a, m), то решение не существует
    if b % gcd_ab_m != 0:
        return None, "Нет решений"

    # Делим на НОД(a, m)
    a //= gcd_ab_m
    b //= gcd_ab_m
    m //= gcd_ab_m

    gcd_val, x, _ = extended_gcd(a, m)

    # Найдем одно решение
    x0 = (x * b) % m
    if x0 < 0:
        x0 += m

    print(f"Одно решение: x ≡ {x0} (mod {m})")
    return x0, m

def solve_congruences_euler(a, b, m):
    # Решение ax ≡ b mod m с использованием формулы Эйлера
    if gcd(a, m) != 1:
        return None, "Нет решений"

    gcd_val, a_inverse, _ = extended_gcd(a, m)

    # Вывод текущих шагов
    print(f"Обратный элемент: {a}^-1 ≡ {a_inverse} (mod {m})")

    a_inverse %= m
    x0 = (a_inverse * b) % m

    print(f"Одно решение (Эйлер): x ≡ {x0} (mod {m})")
    return x0, m

def main(congruences):
    solutions_extended = []
    solutions_euler = []

    for a, b, m in congruences:
        print(f"\nРешаем сравнение: {a}x ≡ {b} mod {m}")

        # Решение методом расширенного алгоритма Евклида
        x0_ext, result_ext = solve_congruences_extended(a, b, m)
        if result_ext == "Нет решений":
            print(f"Расширенный алгоритм: {a}x ≡ {b} mod {m}: {result_ext}")
        else:
            solutions_extended.append((x0_ext, m))

        # Решение методом формулы Эйлера
        x0_euler, result_euler = solve_congruences_euler(a, b, m)
        if result_euler == "Нет решений":
            print(f"Формула Эйлера: {a}x ≡ {b} mod {m}: {result_euler}")
        else:
            solutions_euler.append((x0_euler, m))

def lcm(a, b):
    # Находим НОД двух чисел
    return abs(a * b) // gcd(a, b)

congruences = [
    (6, 7, 22),  # x ≡ 3 mod 5
    #(1, 2, 7),  # x ≡ 2 mod 7
    #(1, 7, 4)  # x ≡ 7 mod 4
]

main(congruences)
