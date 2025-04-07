import sys
import time
import random
from math import isqrt
from datetime import datetime


def is_prime(n, k=5):
    """Тест Міллера-Рабіна"""
    if n < 2:
        return False
    for p in [2, 3, 5, 7, 11, 13, 17, 19, 23]:
        if n % p == 0:
            return n == p
    r, s = 0, n - 1
    while s % 2 == 0:
        r += 1
        s //= 2
    for _ in range(k):
        a = random.randrange(2, n - 1)
        x = pow(a, s, n)
        if x in (1, n - 1):
            continue
        for _ in range(r - 1):
            x = pow(x, 2, n)
            if x == n - 1:
                break
        else:
            return False
    return True


def trial_division(n):
    """Метод пробних ділень"""
    for p in range(2, 48):
        if n % p == 0:
            return p
    return None


def pollards_rho(n):
    """ρ-метод Полларда"""
    if n % 2 == 0:
        return 2
    x = random.randint(2, n - 1)
    y = x
    c = random.randint(1, n - 1)
    d = 1
    while d == 1:
        x = (pow(x, 2, n) + c) % n
        y = (pow(y, 2, n) + c) % n
        y = (pow(y, 2, n) + c) % n
        d = gcd(abs(x - y), n)
        if d == n:
            return None
    return d if d != n else None


def brilhart(n):
    """Простий варіант Брілхарта-Моррісона (як-от алгоритм Діксона)"""
    if n % 2 == 0:
        return 2
    y, c, m = random.randrange(1, n), random.randrange(1, n), random.randrange(1, n)
    g, r, q = 1, 1, 1
    while g == 1:
        x = y
        for _ in range(r):
            y = (pow(y, 2, n) + c) % n
        k = 0
        while k < r and g == 1:
            ys = y
            for _ in range(min(m, r - k)):
                y = (pow(y, 2, n) + c) % n
                q = q * abs(x - y) % n
            g = gcd(q, n)
            k += m
        r *= 2
    if g == n:
        while True:
            ys = (pow(ys, 2, n) + c) % n
            g = gcd(abs(x - ys), n)
            if g > 1:
                break
    return g if g != n else None


def gcd(a, b):
    while b:
        a, b = b, a % b
    return a


def factor(n):
    start_time = datetime.now()
    print(f" Початок факторизації: {start_time}")
    factors = []

    def report(factor, method):
        timestamp = datetime.now()
        print(f"[{timestamp}] Знайдено дільник: {factor} (метод: {method})")
        factors.append(factor)

    def recursive(n):
        if is_prime(n):
            report(n, "Міллера-Рабіна")
            return
        d = trial_division(n)
        if d:
            report(d, "Пробні ділення")
            recursive(n // d)
            return
        d = pollards_rho(n)
        if d:
            report(d, "ρ-метод Полларда")
            recursive(n // d)
            return
        if is_prime(n):
            report(n, "Міллера-Рабіна")
            return
        d = brilhart(n)
        if d:
            report(d, "Метод-алгоритм Діксона")
            recursive(n // d)
        else:
            print("Я не можу знайти канонічний розклад числа :(")

    recursive(n)
    print(f"Канонічний розклад: {sorted(factors)}")
    print(f"Кінець факторизації: {datetime.now()}")
    return factors


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("2500744714570633849")
        sys.exit(1)

    try:
        num = int(sys.argv[1])
        factor(num)
    except ValueError:
     print("Ввести ціле тут число")
