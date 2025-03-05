# Преобразование строки в число.
def str_to_poly(s):
    return int(s, 2) if s else 0

# Преобразование числа в строку с ведущими нулями.
def poly_to_str(p, degree):
    if p == 0:
        return '0' * degree
    return bin(p)[2:].zfill(degree)[-degree:]

# Сложение
def gf_add(a, b):
    return a ^ b

# Умножение
def gf_multiply(a, b, mod_poly):
    mod_degree = mod_poly.bit_length() - 1
    result = 0
    while b:
        if b & 1:
            result ^= a
        a <<= 1
        if a >> mod_degree:
            a ^= mod_poly
        b >>= 1
    return result

# Деление
def gf_divmod(dividend, divisor):
    if divisor == 0:
        raise ValueError("Деление на ноль")
    quotient = 0
    remainder = dividend
    divisor_degree = divisor.bit_length() - 1
    while remainder.bit_length() >= divisor_degree + 1:
        shift = remainder.bit_length() - divisor_degree - 1
        quotient ^= (1 << shift)
        remainder ^= (divisor << shift)
    return quotient, remainder

# НОД
def gf_gcd(a, b):
    while b != 0:
        _, remainder = gf_divmod(a, b)
        a, b = b, remainder
    return a

# Генерация таблицы умножения
def generate_mult_table(mod_poly):
    degree = mod_poly.bit_length() - 1
    elements = list(range(1 << degree))
    table = []
    for a in elements:
        row = []
        for b in elements:
            row.append(gf_multiply(a, b, mod_poly))
        table.append(row)
    return elements, table


def main():
    mod_poly = None
    while True:
        s = input("Введите образующий многочлен: ").strip()
        if all(c in '01' for c in s) and len(s) > 0:
            mod_poly = str_to_poly(s)
            break
        print("Ошибка: введите двоичное число (0 и 1)")

    degree = mod_poly.bit_length() - 1
    print(f"Поле GF(2^{degree}) создано.")

    while True:
        print("\nВыберите операцию:")
        print("1. Сложение")
        print("2. Умножение")
        print("3. Деление")
        print("4. НОД")
        print("5. Таблица умножения")
        print("6. Выход")
        choice = input("> ").strip()

        if choice == '6':
            break

        try:
            if choice in ('1', '2', '3', '4'):
                a = input("Введите первый многочлен: ").strip()
                a = str_to_poly(a)
                b = input("Введите второй многочлен: ").strip()
                b = str_to_poly(b)

            if choice == '1':
                res = gf_add(a, b)
                print(f"Результат: {poly_to_str(res, degree)}")

            elif choice == '2':
                res = gf_multiply(a, b, mod_poly)
                print(f"Результат: {poly_to_str(res, degree)}")

            elif choice == '3':
                quotient, remainder = gf_divmod(a, b)
                print(f"Частное: {poly_to_str(quotient, degree)}, Остаток: {poly_to_str(remainder, degree)}")

            elif choice == '4':
                gcd = gf_gcd(a, b)
                print(f"НОД: {poly_to_str(gcd, degree)}")

            elif choice == '5':
                elements, table = generate_mult_table(mod_poly)
                header = "      " + " ".join(poly_to_str(e, degree).rjust(3) for e in elements)
                print(header)
                for i, row in enumerate(table):
                    row_str = poly_to_str(elements[i], degree).rjust(3) + " | "
                    row_str += " ".join(poly_to_str(num, degree).rjust(3) for num in row)
                    print(row_str)

            else:
                print("Неверный выбор.")
        except Exception as e:
            print(f"Ошибка: {e}")

if __name__ == "__main__":
    main()