# -*- coding: utf-8 -*-
# @Created by PyCharm Community Edition.
# @User: leiyongbo <lyb19900227@126.com>
# @Date: 2017/7/17
# @Time: 16:41
# @url: http://www.lintcode.com/zh-cn/problem/trailing-zeros/
# @Description:

class Solution:
    # @param n a integer
    # @return as a integer
    def trailingZeros(self, n):
        count = 0
        while n > 0:
            count += n / 5
            n /= 5
        return count


if __name__ == '__main__':
    s = Solution()
    print (s.trailingZeros(25))
    # 10 * 9 * 8 * 7 * 6 * 5 * 4 * 3 *2 * 1
    #