# списки
numbers_ = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]

not_primes = []
primes = []

# перебираем список
for i in numbers_:
    if i < 2:
        continue

    is_prime = True

# вложенние циклa
    for j in range(2, i):
        if i % j == 0:
            is_prime = False
            break

# добавляем число
    if is_prime:
        primes.append(i)
    else:
        not_primes.append(i)

# выводим в консоль
print("Primes:", primes)
print("Not Primes:", not_primes)

