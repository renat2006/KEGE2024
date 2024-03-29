from string import ascii_lowercase, digits


def n_to_p(n, p):
    letters = digits + ascii_lowercase
    num = ''
    while n:
        num = letters[n % p] + num
        n //= p
    return num

def f(n):
    f1 = n_to_p(n, 3)
    f2 = f1 + str(n % 3)
    f3 = f2 + str(n % 3)
    return int(f3, 3)
min_v = 1e9
for n in range(1, 100000):
    res = f(n)
    if res < min_v and res > 1000:
        min_v = res
print(min_v)