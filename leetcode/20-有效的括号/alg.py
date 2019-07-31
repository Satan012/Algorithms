class Solution:
    def isValid(self, s):
        leftchar = ['(', '{', '[']
        rightchar = [')', '}', ']']
        stack = []
        top = -1
        flag = True

        for i in range(len(s)):
            if s[i] in leftchar:
                stack.append(s[i])
                top += 1
            elif s[i] in rightchar:
                if top == -1 or stack[top] != leftchar[rightchar.index(s[i])]:
                    flag = False
                    break
                else:
                    del stack[top]
                    top -= 1
        return flag and top == -1


if __name__ == '__main__':
    solution = Solution()

    s = ""

    print(solution.isValid(s))
