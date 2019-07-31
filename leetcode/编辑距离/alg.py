#  reference: https://zhuanlan.zhihu.com/p/43009353
class Solution:
    def minDistance(self, word1, word2):
        m = len(word1)
        n = len(word2)
        print('m', m, 'n', n)
        dp = [[-1] * (n + 1) for _ in range(m + 1)]  # word1[:i+1]到word2[:j+1]的编辑距离

        dp[0][0] = 0  # 无字符串到无字符串的距离是0

        # ------- 初始化操作 -------
        for i in range(1, m + 1):
            dp[i][0] = i  # 使用删除操作
        for j in range(1, n + 1):
            dp[0][j] = j  # 使用添加操作

        # ------- 动态规划 -------
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if word1[i - 1] == word2[j - 1]:
                    replace_cost = 0
                else:
                    replace_cost = 1

                dp[i][j] = min([
                    dp[i][j - 1] + 1,  # 插入操作，word1没有损失，word2被抵消了一个字符
                    dp[i - 1][j] + 1,  # 删除操作，word2没损失，word1被抵消了一个字符
                    dp[i - 1][j - 1] + replace_cost  # replace操作的cost不一定为1
                ])
        return dp[-1][-1]


if __name__ == '__main__':
    solution = Solution()

    word1 = "horse"
    word2 = "ros"

    print(solution.minDistance(word1, word2))
