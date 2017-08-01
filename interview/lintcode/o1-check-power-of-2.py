# -*- coding: utf-8 -*-
# @Created by PyCharm Community Edition.
# @User: leiyongbo <lyb19900227@126.com>
# @Date: 2017/8/1
# @Time: 21:19
# @url: http://www.lintcode.com/zh-cn/problem/o1-check-power-of-2/
# @Description:用 O(1) 时间检测整数 n 是否是 2 的幂次。

class Solution:
    """
    @param n: An integer
    @return: True or false
    """
    def checkPowerOf2(self, n):
        # write your code here
        if n == 0:
            return False
        if n & (n-1) == 0:
            return True
        else:
            return False


if __name__ == '__main__':
    s = Solution()
    print (s.checkPowerOf2(8))