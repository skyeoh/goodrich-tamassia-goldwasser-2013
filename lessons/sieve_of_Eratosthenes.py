def sieve_of_Eratosthenes(n):
    """Print all prime numbers up to n (including n)."""

    prime = [True for i in range(n+1)] # initialize Boolean array
    p = 2
    while p*p < n:      # only check up to sqrt(n)
        # if prime[p] remains True, it is a prime
        if prime[p]:
            # cross out multiples of p
            for i in range(p*2, n+1, p):
                prime[i] = False
        p += 1
    prime[0] = prime[1] = False

    for p in range(n+1): # generate prime numbers
        if prime[p]:
            yield p

if __name__ == "__main__":
    print("n = 1:")
    n = 1
    for i in sieve_of_Eratosthenes(n):
        print(i)

    print("n = 2:")
    n = 2
    for i in sieve_of_Eratosthenes(n):
        print(i)

    print("n = 10:")
    n = 10
    for i in sieve_of_Eratosthenes(n):
        print(i)

    print("n = 30:")
    n = 30
    for i in sieve_of_Eratosthenes(n):
        print(i)
