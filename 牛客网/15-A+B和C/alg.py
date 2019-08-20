def judgeSum(s1, s2, target):
    add = 0
    while len(s1) > 0 and len(s2) > 0 and len(target) > 0:
        cur_sum = int(s1[-1]) + int(s2[-1]) + add
        print(s1, s2, target, cur_sum)
        if cur_sum <= 9 and cur_sum == int(target[-1]):
            add = 0
            s1 = s1[:-1]
            s2 = s2[:-1]
            target = target[:-1]
        else:
            if cur_sum - 10 == int(target[-1]):
                add = 1
                s1 = s1[:-1]
                s2 = s2[:-1]
                target = target[:-1]
            else:
                return False

    if len(target) == 0:
        if len(s1) == 0 and len(s2) == 0:
            if add == 0:  # 全部耗尽，且无余量
                return True
            else:  # 还有一个进位未处理
                return False
        else:
            return False
    else:
        if len(s1) == 0 and len(s2) == 0:
            if add != int(target):
                return False
            else:
                return True
        else:
            rest = int(s1) if len(s1) > 0 else int(s2)
            if rest + add == int(target):
                return True
            else:
                return False


def judgeSubtract(s1, s2, target):
    borrow = 0
    while len(s1) > 0 and len(s2) > 0 and len(target) > 0:
        if int(s1[-1]) - borrow >= int(s2[-1]):
            cur_subtract = int(s1[-1]) - borrow - int(s2[-1])
            borrow = 0
        else:
            cur_subtract = 10 + int(s1[-1]) - borrow - int(s2[-1])
            borrow = 1

        if cur_subtract != int(target[-1]):
            return False
        else:
            s1 = s1[:-1]
            s2 = s2[:-1]
            target = target[:-1]

    if len(target) == 0:
        if len(s1) == 0 and len(s2) == 0:
            if borrow == 0:
                return True
            else:
                return False
        elif len(s1) * len(s2) == 0:  # 有某一个是0
            rest = int(s1) if len(s1) != 0 else int(s2)
            if rest - borrow == 0:
                return True
            else:
                return False
        else:
            if int(s1) - borrow - int(s2) == 0:
                return True
            else:
                return False
    else:
        if len(s1) == 0 and len(s2) == 0:
            return False
        else:
            rest = int(s1) if len(s1) != 0 else int(s2)
            if rest - borrow == 0:
                return True
            else:
                return False


if __name__ == '__main__':
    # num = input()
    # cases = []
    # res = []
    # for i in range(num):
    #     cases.append(input().split(' '))
    #
    # for c in cases:

    s1 = "18"
    s2 = "9"
    target = "9"



