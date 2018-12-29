def fibonacci(number):
    """Defines the n-fibonacci number with a recursion method"""
    fibo = [0 , 1]
    for i in range(2, number + 1):
        fibo.append(fibo[i - 2] + fibo[i - 1])
    return fibo[number]


if __name__ == '__main__':
    n = int(input())
    print(fibonacci(n))
