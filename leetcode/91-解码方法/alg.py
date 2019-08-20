class Solution:
    def numDecodings(self, s):
        length = len(s)

        if length == 0 or int(s) == 0:
            return 0
        if s[0] == "0":
            return 0

        dp = [0] * length
        dp[0] = 1

        for i in range(1, length):
            if s[i] == '0':
                if s[i - 1] == '0':  # a0=0, a1=0
                    return 0
                if int(s[i - 1:i + 1]) > 26:  # a0>2, a1=0
                    return 0
                if int(s[i - 1:i + 1]) <= 26:  # a0<=2, a1=0
                    if i > 1:
                        dp[i] = dp[i - 2]
                    else:
                        dp[i] = 1
            elif s[i] != '0':
                if s[i - 1] == '0':
                    if i > 1:
                        dp[i] = dp[i - 2]
                    else:
                        return 0
                if s[i - 1] != '0':
                    if int(s[i - 1: i + 1]) > 26:
                        dp[i] = dp[i - 1]
                    else:
                        dp[i] = dp[i - 1] + dp[i - 2]
        return dp[-1]


if __name__ == '__main__':
    solution = Solution()

    s = "26"

    print(solution.numDecodings(s))
