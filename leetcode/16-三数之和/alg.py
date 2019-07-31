from __future__ import division, print_function, absolute_import
import tensorflow as tf
import numpy as np


class Solution:
    def findPair(self, nums, center_idx, results, length, target=0):
        left = center_idx + 1
        right = length - 1
        while left < right:
            sum2 = nums[left] + nums[right] + nums[center_idx]
            if sum2 == target:
                results.append([nums[center_idx], nums[left], nums[right]])
                print('center:', nums[center_idx], 'left:', nums[left], 'right:', nums[right])
                left += 1
                right -= 1
                while left < right and nums[left - 1] == nums[left] and nums[right] == nums[right + 1]:
                    left += 1
                    right -= 1
            elif sum2 < target:
                left += 1
            else:
                right -= 1

    def threeSum(self, nums):
        nums = sorted(nums)

        results = []
        length = len(nums)

        for idx, n in enumerate(nums):
            if idx == 0 or nums[idx] != nums[idx - 1]:
                self.findPair(nums, idx, results, length)
            else:
                continue

        return results


if __name__ == '__main__':
    solution = Solution()
    x = [-2, 0, 0, 2, 2]
    print(solution.threeSum(x))

