import sys 

def fib(n):
    result = []
    a, b = 0, 1
    while a < n:
        result.append(a)
        a, b = b, a + b
    return result


if __name__ == "__main__":
    f = fib(int(sys.argv[1]))
    print(f)
