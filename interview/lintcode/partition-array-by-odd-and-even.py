# -*- coding: utf-8 -*-
# @Created by PyCharm Community Edition.
# @User: leiyongbo <lyb19900227@126.com>
# @Date: 2017/7/31
# @Time: 17:06
# @url: http://www.lintcode.com/zh-cn/problem/partition-array-by-odd-and-even/
# @Description:分割一个整数数组，使得奇数在前偶数在后。

class Solution:
    # @param nums: a list of integers
    # @return: nothing
    def partitionArray(self, nums):
        # write your code here
        i = 0
        lenght = len(nums)
        moves = 0
        while i < (lenght - moves):
            number = nums[i]
            if 0 == number % 2:
                del nums[i]
                nums.append(number)
                moves += 1
            else:
                i += 1
        return nums


if __name__ == '__main__':
    s = Solution()
    print (s.partitionArray([1, 2, 3, 4]))