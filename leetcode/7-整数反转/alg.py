class Solution:
    def reverse(self, x):
        NEG = 1
        if x < 0:
            x = abs(x)
            NEG = -1
        exp = pow(2, 31)
        down_bound = -1 * exp // 10
        up_bound = exp - 1 // 10

        positive_int = (exp - 1) % 10
        negtive_int = -1 * (exp % 10)

        ans = 0
        while x != 0:
            pop = int(x % 10)
            if ans > up_bound or (ans == up_bound and pop > positive_int):
                return 0
            elif ans < down_bound or (ans == down_bound and pop < negtive_int):
                return 0
            ans = ans * 10 + pop
            x = x // 10
        return ans * NEG


if __name__ == '__main__':
    solution = Solution()
    num = 1534236469
    print(solution.reverse(num))
