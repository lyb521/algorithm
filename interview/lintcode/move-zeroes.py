# -*- coding: utf-8 -*-
# @Created by PyCharm Community Edition.
# @User: leiyongbo <lyb19900227@126.com>
# @Date: 2017/8/16
# @Time: 18:16
# @url: http://www.lintcode.com/zh-cn/problem/move-zeroes/
# @Description:给一个数组 nums 写一个函数将 0 移动到数组的最后面，非零元素保持原数组的顺序


class Solution:
    # @param {int[]} nums an integer array
    # @return nothing, do this in-place
    def moveZeroes(self, nums):
        # Write your code here
        i = 0
        n = 0
        while i < len(nums):
            if nums[i] == 0:
                nums.append(nums[i])
                del(nums[i])
            else:
                i += 1
            n += 1
            if n == len(nums):
                return nums


if __name__ == '__main__':
    s = Solution()
    print (s.moveZeroes([0, 1, 0, 3, 12]))