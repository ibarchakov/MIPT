import sys

depth = 0

def fac(n):
    """Determines the recursion depth"""
    global depth
    if n == 0:
        pass
    else:
        n * fac(n - 1)
        depth += 1
    return int(depth / 2)

def test(function):
    global depth
    print('test #1: ', end='')
    n = 7
    limit = sys.getrecursionlimit()
    try:
        function(n)
    except RuntimeError:
            print('recursion depth exceeded the limit of', sys.getrecursionlimit())
    else:
        print('recursion depth is', function(n), 'not exceeded the limit of',
          sys.getrecursionlimit())
    depth = 0

    print('test #2: ', end='')
    n = 0
    limit = sys.getrecursionlimit()
    try:
        function(n)
    except RuntimeError:
            print('recursion depth exceeded the limit of', sys.getrecursionlimit())
    else:
        print('recursion depth is', function(n), 'not exceeded the limit of',
          sys.getrecursionlimit())
    depth = 0

    print('test #3: ', end='')
    n = -5
    limit = sys.getrecursionlimit()
    try:
        function(n)
    except RuntimeError:
            print('recursion depth exceeded the limit of', sys.getrecursionlimit())
    else:
        print('recursion depth is', function(n), 'not exceeded the limit of',
          sys.getrecursionlimit())
    depth = 0


if __name__ == '__main__':
    test(fac)
