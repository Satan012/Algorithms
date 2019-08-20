# A1 = 能被5整除的数字中所有偶数的和；
# A2 = 将被5除后余1的数字按给出顺序进行交错求和，即计算n1-n2+n3-n4...；
# A3 = 被5除后余2的数字的个数；
# A4 = 被5除后余3的数字的平均数，精确到小数点后1位；
# A5 = 被5除后余4的数字中最大数字。


if __name__ == '__main__':
    flags = [False] * 5

    a1 = 0

    a2 = 0
    sign2 = 1

    a3 = 0

    a4 = 0
    l4 = 0

    a5 = -1

    x = input()
    if x[0] != "0":
        x = x.split(" ")
        x = [int(xx) for xx in x]
        N = x[0]
        x = x[1:]
        # print(x)

        for xx in x:
            tmp = xx % 5
            if tmp == 0:
                if xx % 2 == 0:
                    a1 += xx
                    flags[0] = True
            elif tmp == 1:
                a2 += sign2 * xx
                sign2 *= -1
                flags[1] = True
            elif tmp == 2:
                a3 += 1
                flags[2] = True
            elif tmp == 3:
                a4 += xx
                l4 += 1
                flags[3] = True
            else:
                if xx > a5:
                    a5 = xx
                    flags[4] = True

    res = [a1, a2, a3, a4, a5]
    for i in range(5):
        # print(flags[i])
        if flags[i] is False:
            res[i] = 'N'
    if res[3] == 'N':
        print('{} {} {} {} {}'.format(res[0], res[1], res[2], res[3], res[4]))
    else:
        print('{} {} {} {:.1f} {}'.format(res[0], res[1], res[2], res[3] / l4, res[4]))
