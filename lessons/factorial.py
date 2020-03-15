# Goodrich, Tamassia, Goldwasser (2013) Code Fragment 4.1 on page 150

def factorial(n):
    if n == 0:
        return 1
    else:
        return n*factorial(n-1)

def iterative_factorial(n):
    answer = 1
    while n != 0:
        answer *= n
        n -= 1
    return answer

if __name__ == "__main__":
    for n in range(11):
        print()
        print("[recursive] factorial(" + str(n) + ") =", factorial(n))
        print("[iterative] factorial(" + str(n) + ") =", iterative_factorial(n))
