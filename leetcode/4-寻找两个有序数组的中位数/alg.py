class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        n = len(nums1)
        m = len(nums2)

        IN_MAX = float('inf')
        IN_MIN = float('-inf')

        if n > m:
            return self.findMedianSortedArrays(nums2, nums1)

        LMax1 = LMax2 = RMin1 = RMin2 = 0

        start1 = 0  # 设定填充，确保每个数组是奇数
        rear1 = 2 * n

        while start1 <= rear1:
            c1 = (start1 + rear1) // 2
            c2 = n + m - c1  # 因为一共2n+2m+2个数，所以分割的左侧一共是n+m+1个数，index到n+m

            LMax1 = IN_MIN if c1 == 0 else nums1[(c1 - 1) // 2]
            LMax2 = IN_MIN if c2 == 0 else nums2[(c2 - 1) // 2]
            RMin1 = IN_MAX if c1 == 2 * n else nums1[c1 // 2]
            RMin2 = IN_MAX if c2 == 2 * m else nums2[c2 // 2]

            if LMax1 > RMin2:
                rear1 = c1 - 1
            elif LMax2 > RMin1:
                start1 = c1 + 1
            else:
                break
        return (max(LMax1, LMax2) + min(RMin1, RMin2)) / 2


if __name__ == '__main__':
    solution = Solution()

    nums1 = []
    nums2 = [1]

    print(solution.findMedianSortedArrays(nums1, nums2))
