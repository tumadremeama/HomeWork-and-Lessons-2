def generate_password(n):
    result = ""

    pairs = []
    for i in range (1, 21):
        for j in range (i + 1, 21):
            pairs.append((i, j))

    for pair in pairs:
        pair_sum = sum(pair)
        if n % pair_sum == 0:
            result += f"{pair[0]}{pair[1]}"

    return result

n = 9
password = generate_password(n)
print(password)

n = 11
password = generate_password(n)
print(password)

