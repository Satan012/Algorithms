def maxMulti(n):
    if n < 2:
        return 0
    if n == 2:
        return 1
    if n == 3:
        return 2

    f = [1] * (n + 1)
    f[1] = 1
    f[2] = 2
    f[3] = 3

    for i in range(4, n + 1):
        mid = i // 2
        for j in range(1, mid + 1):
            if f[j] * f[i - j] > f[i]:
                f[i] = f[j] * f[i - j]
    return f[n]


if __name__ == '__main__':
    print(maxMulti(8))
