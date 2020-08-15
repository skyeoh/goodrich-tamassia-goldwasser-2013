# Goodrich, Tamassia, Goldwasser (2013) Code Fragment 13.2 on page 588

def find_boyer_moore(T, P):
    """Return the lowest index of T at which substring P begins (or else -1)."""
    n, m = len(T), len(P)                                 # introduce convenient notations
    if m == 0: return 0                                    # trivial search for empty string
    last = {}                                                    # build 'last' dictionary
    for k in range(m):
        last[P[k]] = k                                        # later occurrence overwrites
    # align end of pattern at index m-1 of text
    i = m-1                                                      # an index into T
    k = m-1                                                     # an index into P
    while i < n:
        if T[i] == P[k]:                                      # a matching character
            if k == 0:
                return i                                          # pattern begins at index i of text
            else:
                i -= 1                                             # examine previous character
                k -= 1                                            # of both T and P
        else:
            j = last.get(T[i], -1)                           # last(T[i]) is -1 if not found
            i += m - min(k, j+1)                          # case analysis for jump step
            k = m-1                                              # restart at end of pattern
    return -1

if __name__ == "__main__":
        T = "I love apples, oranges and blueberries. I dislike durians and grapes."
        P1 = "apples"
        P2 = "pears"
        P3 = " and grapes"
        P4 = ""
        P5 = "tangerines"
        P6 = "d"
        P7 = "is"
        P8 = "  "

        print(find_boyer_moore(T, P1))            # return 7
        print(find_boyer_moore(T, P2))            # return -1
        print(find_boyer_moore(T, P3))            # return 57
        print(find_boyer_moore(T, P4))            # return 0
        print(find_boyer_moore(T, P5))            # return -1
        print(find_boyer_moore(T, P6))            # return 25
        print(find_boyer_moore(T, P7))            # return 43
        print(find_boyer_moore(T, P8))            # return -1
