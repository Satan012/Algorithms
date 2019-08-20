def convertToTen(num, jinzhi):
    l = len(num) - 1
    res = 0
    for idx, n in enumerate(num):
        res += pow(jinzhi, (l - idx)) * int(n)
    return res


if __name__ == '__main__':
    flag = False

    x = 13
    y = 7
    s = "1016"

    print(convertToTen("1016", 13))
    exit(0)

    small = x if x < y else y
    large = x if x > y else y

    div = 0

    for idx, ss in enumerate(s):  # 争取左边小右边大
        if int(ss) > small - 1:
            div = idx
            break
        div += 1

    left = convertToTen(s[:div], small) if div > 0 else 0
    right = convertToTen(s[div:], large) if div < len(s) - 1 else 0

    while left != right:
        print(left, right, div)
        if left > right:
            left = (left - int(s[div-1])) // small
            right = right * large + int(s[div - 1])
            div -= 1
        else:
            left = left * small + int(s[div + 1])
            right = right - int(s[div+1])
            div += 1
    print(left)
