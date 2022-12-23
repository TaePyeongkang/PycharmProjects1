def fib(n):
    a, b = 1, 1
    if n == 1 or n == 2:
        return 1

    for i in range(1, n):
        a, b = b, a + b

    return a
n = int(input('숫자를 입력하세요'))
print(fib(n))
