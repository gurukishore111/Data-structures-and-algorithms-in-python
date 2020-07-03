# n is no of disk #start A #end C #middle B is tower
def hanoi(n, start, middle, end):
    if n == 1:
        print("Move %i from %s to tower %s" % (n, start, end))
    else:
        hanoi(n - 1, start, middle, end)
        print("Move %i from %s to tower %s" % (n, start, end))
        hanoi(n - 1, start, end, middle)


hanoi(3, "A", "B", "C")
