# -*- coding: utf-8 -*-
# @Created by PyCharm Community Edition.
# @User: leiyongbo <lyb19900227@126.com>
# @Date: 2017/7/17
# @Time: 14:31
# @url: http://www.lintcode.com/zh-cn/problem/rotate-string/
# @Description:

class Solution:
    # @param s: a list of char
    # @param offset: an integer
    # @return: nothing

    def rotateString(self, s, offset):
        # write you code here
        length = len(s)
        return s[length-offset:length]+s[0:length-offset]

if __name__ == '__main__':
    s = Solution()
    print  s.rotateString("abcdefg", 1)