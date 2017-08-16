# -*- coding: utf-8 -*-
# @Created by PyCharm Community Edition.
# @User: leiyongbo <lyb19900227@126.com>
# @Date: 2017/8/16
# @Time: 15:52
# @url: http://www.lintcode.com/zh-cn/problem/add-digits/
# @Description:给定一个非负数，表示一个数字数组，在该数的基础上+1，返回一个新的数组。


class Solution:
    # @param {int} num a non-negative integer
    # @return {int} one digit
    def addDigits(self, num):
        # Write your code here
        if num < 10:
            return num
        return (num - 1) % 9 + 1


if __name__ == '__main__':
    s = Solution()
    print (s.addDigits(38))