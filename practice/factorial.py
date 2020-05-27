def factorial(N):
    factorial = 1
    for i in range(1, N+1):
        factorial *= i
    return factorial

factorial_3 = factorial(3)
