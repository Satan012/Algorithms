import sys

if __name__ == '__main__':
    inputs = []
    n = int(sys.stdin.readline().strip())

    for i in range(n):
        # 读取每一行
        line = sys.stdin.readline().strip()
        inputs.append(line)

    for x in inputs:

        count = 1
        start = -1
        records = []

        for i in range(1, len(x)):
            if ord(x[i]) - ord(x[i - 1]) == 1:
                if start == -1:
                    start = i - 1
                count += 1
            else:
                if count >= 4:
                    records.append((start, i - 1))

                start = -1
                count = 1

        bias = 0
        for r in records:
            real_r = r[0] - bias
            length = r[1] - r[0] + 1
            x = x.replace(x[real_r + 1:real_r + length - 1], '-')
            bias += length - 3
        print(x)
