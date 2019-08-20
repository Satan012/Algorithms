import sys

if __name__ == '__main__':
    n = int(sys.stdin.readline().strip())

    moneys = []

    for i in range(n):
        line = sys.stdin.readline().strip()
        moneys.append(line)

    gaps = {
        0: 0,
        3000: 3,
        12000: 10,
        25000: 20,
        35000: 25,
        55000: 30,
        80000: 35,
    }

    lst = list(gaps)

    moneys = [float(m) - 5000 for m in moneys]
    res = []
    for m in moneys:
        tax = 0
        if m == 0:
            res.append(0)
            continue

        for i in range(1, len(lst) - 1):
            if lst[i - 1] < m <= lst[i]:
                tax = tax + (m - lst[i - 1]) * (gaps[lst[i]] * 0.01)
                break
            else:
                tax = tax + (lst[i] - lst[i - 1]) * (gaps[lst[i]] * 0.01)

        if m > lst[-1]:
            tax += (m - lst[-1]) * 0.45

        str_tax = str(tax)
        str_tax = str_tax.split('.')
        if len(str_tax) > 1:
            if int(str_tax[1][0]) < 5:
                res.append(int(str_tax[0]))
            else:
                res.append(int(str_tax[0]) + 1)

        else:
            res.append(int(str_tax[0]))

    for r in res:
        print(r)
