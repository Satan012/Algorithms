class Solution:
    def threeSumClosest(self, nums, target):
        nums.sort()  # O(nlogn)

        result = sum(nums[:3])  # 初始值
        min_gap = abs(target - result)

        length = len(nums)
        for i in range(length-2):  # O(n^2)
            if i > 0 and nums[i] == nums[i-1]:
                continue

            l = i + 1
            r = length - 1

            while l < r:  # 因为唯一解，因此不需要考虑去重
                tmp = nums[i] + nums[l] + nums[r]
                tmp_gap = abs(target - tmp)
                if tmp_gap < min_gap:
                    min_gap = tmp_gap
                    result = tmp

                if tmp < target:
                    l += 1
                elif tmp > target:
                    r -= 1
                else:
                    return result
        return result


if __name__ == '__main__':
    solution = Solution()

    nums = [-1]
    target = 1
    print(solution.threeSumClosest(nums, target))