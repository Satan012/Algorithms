class Solution:
    def isInterleave(self, s1, s2, s3):  # 回溯，leetcode超时
        l1 = len(s1)
        l2 = len(s2)
        l3 = len(s3)

        if l1 == l2 == l3 == 0:
            return True
        if l1 == 0 and l2 != 0 and l2 != l3:
            return False
        if l1 != 0 and l2 == 0 and l1 != l3:
            return False

        flag1 = flag2 = False

        if l1 > 0 and s1[0] == s3[0]:
            flag1 = self.isInterleave(s1[1:], s2, s3[1:])
        if l2 > 0 and s2[0] == s3[0]:
            flag2 = self.isInterleave(s1, s2[1:], s3[1:])

        return flag1 or flag2

    def isInterleave_1(self, s1, s2, s3):
        l1 = len(s1)
        l2 = len(s2)
        l3 = len(s3)

        if l3 != l1 + l2:
            return False

        dp = [[False] * (l2 + 1) for _ in range(l1 + 1)]
        dp[0][0] = True

        for i in range(0, l1 + 1):
            for j in range(0, l2 + 1):

                tmp1 = tmp2 = False

                if i > 0:
                    tmp1 = dp[i - 1][j] and s1[i - 1] == s3[i + j - 1]
                if j > 0:
                    tmp2 = dp[i][j - 1] and s2[j - 1] == s3[i + j - 1]

                if i > 0 or j > 0:
                    dp[i][j] = tmp1 or tmp2

        return dp[-1][-1]


if __name__ == '__main__':
    solution = Solution()

    # s1 = "abbbbbbcabbacaacccababaabcccabcacbcaabbbacccaaaaaababbbacbb"
    # s2 = "ccaacabbacaccacababbbbabbcacccacccccaabaababacbbacabbbbabc"
    # s3 = "cacbabbacbbbabcbaacbbaccacaacaacccabababbbababcccbabcabbaccabcccacccaabbcbcaccccaaaaabaaaaababbbbacbbabacbbacabbbbabc"
    #
    # print(solution.isInterleave(s1, s2, s3))

    s1 = "aabcc"
    s2 = "dbbca"
    s3 = "aadbbcbcac"

    print(solution.isInterleave_1(s1, s2, s3))
