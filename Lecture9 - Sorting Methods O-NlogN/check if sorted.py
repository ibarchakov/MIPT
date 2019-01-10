def check_sorted(a, ascending=True):
    """Checks if list A is sorted for O(N)"""
    flag = True
    s = 2 * int(ascending) - 1
    for i in range(0, len(a) - 1):
        if s * a[i] > s * a[i + 1]:
            flag = False
            break
    return flag


if __name__ == '__main__':
    a = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    b = [0, 1, 2, 3, 4, 5, 6, 8, 7, 9]
    print(check_sorted(a))
    print(check_sorted(b))
