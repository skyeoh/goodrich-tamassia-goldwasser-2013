# Goodrich, Tamassia, Goldwasser (2013) Code Fragments 13.3-13.4 on pages 591-592

def find_kmp(T, P):
    """Return the lowest index of T at which substring P begins (or else -1)."""
    n, m = len(T), len(P)                                  # introduce convenient notations
    if m == 0: return 0                                      # trivial search for empty string
    fail = compute_kmp_fail(P)                       # rely on utility to precompute
    j = 0                                                            # index into text
    k = 0                                                           # index into pattern
    while j < n:
        if T[j] == P[k]:                                       # P[0:1+k] matched thus far
            if k == m-1:                                        # match is complete
                return j-m+1
            j += 1                                                  # try to extend match
            k += 1
        elif k > 0:
            k = fail[k-1]                                         # reuse suffix of P[0:k]
        else:
            j += 1
    return -1                                                       # reached end without match

def compute_kmp_fail(P):
    """Utility that computes and returns KMP 'fail' list."""
    m = len(P)
    fail = [0] * m                          # by default, presume overlap of 0 everywhere
    j = 1
    k = 0
    while j < m:                            # compute f(j) during this pass, if nonzero
        if P[j] == P[k]:                    # k + 1 characters match thus far
            fail[j] = k+1
            j += 1
            k += 1
        elif k > 0:                            # k follows a matching prefix
            k = fail[k-1]
        else:                                    # no match found starting at j
            j += 1
    return fail

if __name__ == "__main__":
    # Test 1
    T = "I love apples, oranges and blueberries. I dislike durians and grapes."
    P1 = "apples"
    P2 = "pears"
    P3 = " and grapes"
    P4 = ""
    P5 = "tangerines"
    P6 = "d"
    P7 = "is"
    P8 = "  "

    print(find_kmp(T, P1))            # return 7
    print(find_kmp(T, P2))            # return -1
    print(find_kmp(T, P3))            # return 57
    print(find_kmp(T, P4))            # return 0
    print(find_kmp(T, P5))            # return -1
    print(find_kmp(T, P6))            # return 25
    print(find_kmp(T, P7))            # return 43
    print(find_kmp(T, P8))            # return -1

    # Test 2
    T = "amal amalga amalgama amalgama amalgamation amalagamation amal"
    P9 = "amalgamation"
    P10 = "amalgamations"

    print()
    print(find_kmp(T, P9))               # return 30
    print(find_kmp(T, P10))             # return -1
