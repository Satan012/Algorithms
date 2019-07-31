class Solution:
    def maxArea(self, height):
        """
        双指针，移动短的那边，这样虽然底边长度减小，但是高可能增加
        :param height:
        :return:
        """
        left = 0
        right = len(height) - 1
        maxArea = 0
        while left < right:
            b = right - left
            if height[left] < height[right]:
                h = height[left]
                left += 1
            else:
                h = height[right]
                right -= 1
            area = h * b
            if area > maxArea:
                maxArea = area
        return maxArea


if __name__ == '__main__':
    solution = Solution()

    height = [1, 8, 6, 2, 5, 4, 8, 3, 7]
    print(solution.maxArea(height))
