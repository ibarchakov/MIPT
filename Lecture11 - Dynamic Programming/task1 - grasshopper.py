def grasshoper(n):
    """There is a grasshopper sitting on a number line.
    It can jump to the right with a step '+1' '+2' or '+3'. At first it sits at a point '1'.
    Determine the number of different routes that lead a grasshopper to the point 'n'.

    Label the number of routes to point 'n' as k[n].
    Note: there is one route from '1' to '1' -- it contains no jumps.
    It can jump to point '2' in a single way -- from point '1'.

    Since a grasshopper can make only '+1' '+2' and '+3' steps then the number of
    routes leading to point 'n' is a summ of number of routes to points 'n-1'
    'n-2' and 'n-3'.
    k[n] = k[n-1] + k[n-2] + k[n-3] -- reccurent relation

    """
    k = [0, 1, 1] + [0] * n
    for i in range(3, n + 1):
        k[i] = k[i - 1] + k[i - 2] + k[i - 3]
    return k[n]

def main():
    n = int(input('Enter n point: '))
    print(grasshoper(n))


if __name__ == '__main__':
    main()
