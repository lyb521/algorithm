# -*- coding: utf-8 -*-
# @Created by PyCharm Community Edition.
# @User: leiyongbo <lyb19900227@126.com>
# @Date: 2017/7/17
# @Time: 12:19
# @url: http://www.lintcode.com/zh-cn/problem/unique-characters/
# @Description:

class Solution:
    # @param s: a string
    # @return: a boolean
    def isUnique(self, str):
        # write your code here
        for i in xrange(0, len(str)):
            if str.find(str[i], i+1) > -1:
                return False
        return True

if __name__ == '__main__':
    s = Solution()
    print (s.isUnique("abc"))