class Solution:
    def isScramble(self, s1, s2):
        # print(s1, s2)

        len_1 = len(s1)
        len_2 = len(s2)

        if len_1 != len_2:
            return False

        if s1 == s2:
            return True

        if len_1 == len_2 == 1:
            return s1 == s2

        if len_1 == len_2 == 2:
            return s1 == s2 or s1 == s2[::-1]  # 要么相等要么逆序

        for i in range(1, len(s1)):

            mid = i

            tmp1 = self.isScramble(s1[:mid], s2[:mid])
            tmp2 = self.isScramble(s1[mid:], s2[mid:])

            tmp3 = self.isScramble(s1[:mid], s2[len_2-mid:])
            tmp4 = self.isScramble(s1[mid:], s2[:len_2-mid])

            # print(tmp1, tmp2, tmp3, tmp4)

            if (tmp1 and tmp2) or (tmp3 and tmp4):
                return True

        return False


if __name__ == '__main__':
    solution = Solution()

    s1 = "abcdefghijklmn"
    s2 = "efghijklmncadb"

    print(solution.isScramble(s1, s2))
