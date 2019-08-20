# reference: https://blog.csdn.net/qq_17550379/article/details/85093224

class Solution:
    def largestRectangleArea(self, heights):
        stack = []  # 生序栈，只会添加比当前元素大的元素，放进去后，填出柱子可以形成的面积时该柱子及所有右边的柱子组成的
        res = 0
        i = 0

        while i < len(heights):
            if not stack or heights[i] >= heights[stack[-1]]:
                stack.append(i)
                i += 1
            else:
                k = stack.pop()

                # 第一个被压入的元素和最后被弹出的元素会面临栈为空，最后被弹出的元素时最小的元素，因此可以乘总长度
                res = max(res, heights[k] * ((i - stack[-1] - 1) if stack else i))

        while stack:
            k = stack.pop()
            res = max(res, heights[k] * ((i - stack[-1] - 1) if stack else i))
        return res


if __name__ == '__main__':
    solution = Solution()

    x = [2, 1, 5, 6, 2, 3]

    print(solution.largestRectangleArea(x))
