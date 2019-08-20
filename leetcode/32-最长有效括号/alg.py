# -*- coding:utf-8 -*-
from __future__ import division, print_function, absolute_import
import numpy as np


class Solution:
    def longestValidParentheses(self, s):  # 动态规划，自低向上
        length = len(s)
        if length == 0:
            return 0
        dp = [0] * length  # 0～i最长的有效括号长度
        for i in range(1, length):
            if s[i] == ')':
                if s[i - 1] == '(':
                    dp[i] = dp[i - 2] + 2
                elif s[i - 1] == ')' and i - dp[i - 1] - 1 >= 0 and s[i - dp[i - 1] - 1] == '(':
                    dp[i] = dp[i - dp[i - 1] - 2] + (dp[i - 1] + 2)
        return max(dp)


if __name__ == '__main__':
    solution = Solution()

    s = "(()))())("

    print(solution.longestValidParentheses(s))
