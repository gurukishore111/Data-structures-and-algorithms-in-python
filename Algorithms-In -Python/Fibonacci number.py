# Fibonacci number
# 0 1 1 2 3 5 8 13
def fab(n):
    a = 0
    b = 1
    for i in range(2, n):
        c = a + b
        a = b
        b = c
        print(c)


fab(100)
