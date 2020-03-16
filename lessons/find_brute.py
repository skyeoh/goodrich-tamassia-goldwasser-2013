# Goodrich, Tamassia, Goldwasser (2013) Code Fragment 13.1 on page 584

def find_brute(T, P):
    """Return the lowest index of T at which substring P begins (or else -1)."""
    n, m = len(T), len(P)                   # introduce convenient notations
    for i in range(n-m+1):                 # try every potential starting index within T
        k = 0                                        # an index into pattern P
        while k < m and T[i + k] == P[k]:                  # kth character of P matches
            k += 1
        if k == m:                                # if we reached the end of the pattern,
            return i                                 # substring T[i:i+m] matches P
    return -1                                       # failed to find a match starting with any i

if __name__ == '__main__':
    T = "I love apples, oranges and blueberries. I dislike durians and grapes."
    P1 = "apples"
    P2 = "pears"
    P3 = " and grapes"
    P4 = ""
    P5 = "tangerines"
    P6 = "d"
    P7 = "is"
    P8 = "  "

    print(find_brute(T, P1))            # return 7
    print(find_brute(T, P2))            # return -1
    print(find_brute(T, P3))            # return 57
    print(find_brute(T, P4))            # return 0
    print(find_brute(T, P5))            # return -1
    print(find_brute(T, P6))            # return 25
    print(find_brute(T, P7))            # return 43
    print(find_brute(T, P8))            # return -1
