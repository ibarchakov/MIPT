def merge(a, b):
    """Merging of two sorted lists A and B into list C"""
    c = [0] * (len(a) + len(b))
    i = k = n = 0
    while i < len(a) and k < len(b):
        if a[i] <= b[k]:
            c[n] = a[i]
            i += 1
            n += 1
        else:
            c[n] = b[k]
            k += 1
            n += 1
    while i < len(a):
        c[n] = a[i]
        i += 1
        n += 1
    while k < len(b):
        c[n] = b[k]
        k += 1
        n += 1
    return c


def merge_sort(a):
    """Recursively sorts A list with a merge sort"""
    if len(a) <= 1:
        return
    middle = len(a) // 2
    left = [a[i] for i in range(0, middle)]
    right = [a[i] for i in range(middle, len(a))]
    merge_sort(left)
    merge_sort(right)
    c = merge(left, right)
    for i in range(len(a)):
        a[i] = c[i]
    return a


if __name__ == '__main__':
    a = [4, 7, 2, 9, 1, 0, 5, 3]
    a = merge_sort(a)
    print(a)
