# -*- coding: utf-8 -*-
# @Created by PyCharm Community Edition.
# @User: leiyongbo <lyb19900227@126.com>
# @Date: 2017/7/14
# @Time: 16:01
# @url: http://www.lintcode.com/zh-cn/problem/first-position-unique-character/
# @Description:

class Solution:
    # @param {string} s a string
    # @return {int} it's index
    def firstUniqChar(self, s):
        # Write your code here
        if not s:
            return -1
        for i in xrange(0, len(s)) :
            if s.find(s[i],0, i) == -1 and s.find(s[i], i+1) == -1:
                return i
        return -1


if __name__ == '__main__':
    s = Solution()
    print  s.firstUniqChar("{{;;lintcodelintcode}}")