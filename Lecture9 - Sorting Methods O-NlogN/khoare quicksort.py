def khoare_sort(a):
    """Sorts the A list with a Tony Khoare quicksort algorithm:
    recursively divides the list into three lists comparing with
    a barrier element

    """
    if len(a) <= 1:
        return
    barrier = a[0]
    left = []
    middle = []
    right = []
    for x in a:
        if x < barrier:
            left.append(x)
        elif x == barrier:
            middle.append(x)
        else:
            right.append(x)
    khoare_sort(left)
    khoare_sort(right)
    k = 0
    for x in left + middle + right:
        a[k] = x
        k += 1
    return a


if __name__ == '__main__':
    a = [3, 9, 1, 0, 5, 8, 2, 4, 7]
    khoare_sort(a)
    print(a)
