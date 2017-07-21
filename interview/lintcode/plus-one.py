# -*- coding: utf-8 -*-
# @Created by PyCharm Community Edition.
# @User: leiyongbo <lyb19900227@126.com>
# @Date: 2017/7/10
# @Time: 14:34
# @url: http://www.lintcode.com/zh-cn/problem/plus-one/
# @Description:给定一个非负数，表示一个数字数组，在该数的基础上+1，返回一个新的数组。

class Solution:
    # @param {int[]} digits a number represented as an array of digits
    # @return {int[]} the result


    def plusOne(self, digits):
        # Write your code here
        number = 0
        length = len(digits)
        for i in range(0, length):
            number += digits[length - i - 1] * pow(10, i)
        number += 1
        return map(int, list(str(number)))


if __name__ == '__main__':
    s = Solution()
    print (s.plusOne([1, 2, 3]))
