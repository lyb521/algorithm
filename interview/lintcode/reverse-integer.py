# -*- coding: utf-8 -*-
# @Created by PyCharm Community Edition.
# @User: leiyongbo <lyb19900227@126.com>
# @Date: 2017/7/19
# @Time: 18:05
# @url: http://www.lintcode.com/zh-cn/problem/reverse-integer/
# @Description:将一个整数中的数字进行颠倒，当颠倒后的整数溢出时，返回 0 (标记为 32 位整数)。

class Solution:
    # @param {int} n the integer to be reversed
    # @return {int} the reversed integer
    def reverseInteger(self, n):
        # Write your code here
        if n < 0:
            old_n = abs(n)
        else:
           old_n = n
        reverse = 0
        while old_n > 0:
            reverse = reverse * 10 + old_n % 10
            old_n /= 10
        if reverse > 2147483647:
            return 0
        if n < 0:
            return  -reverse
        else:
            return reverse

if __name__ == '__main__':
    s = Solution()
    print ((s.reverseInteger(1534236469)))