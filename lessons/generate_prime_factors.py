def generate_prime_factors(n):
    """Generate prime factors of a positive integer n."""
    p = 1
    while p <= n:
        p += 1
        if n % p == 0:
            yield p
            n = n/p
            p = 1           # start over

if __name__ == "__main__":
    n = 1
    print("Prime factors of", n)
    for i in generate_prime_factors(n):
        print(i)

    n = 2
    print("Prime factors of", n)
    for i in generate_prime_factors(n):
        print(i)

    n = 3
    print("Prime factors of", n)
    for i in generate_prime_factors(n):
        print(i)

    n = 5
    print("Prime factors of", n)
    for i in generate_prime_factors(n):
        print(i)

    n = 13
    print("Prime factors of", n)
    for i in generate_prime_factors(n):
        print(i)

    n = 64
    print("Prime factors of", n)
    for i in generate_prime_factors(n):
        print(i)

    n = 81
    print("Prime factors of", n)
    for i in generate_prime_factors(n):
        print(i)

    n = 1092
    print("Prime factors of", n)
    for i in generate_prime_factors(n):
        print(i)

    n = 35
    print("Prime factors of", n)
    for i in generate_prime_factors(n):
        print(i)

    n = 72
    print("Prime factors of", n)
    for i in generate_prime_factors(n):
        print(i)

    n = 189
    print("Prime factors of", n)
    for i in generate_prime_factors(n):
        print(i)

    n = 232321
    print("Prime factors of", n)
    for i in generate_prime_factors(n):
        print(i)

    n = 67232321
    print("Prime factors of", n)
    for i in generate_prime_factors(n):
        print(i)
