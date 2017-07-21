# -*- coding: utf-8 -*-
# @Created by PyCharm Community Edition.
# @User: leiyongbo <lyb19900227@126.com>
# @Date: 2017/7/14
# @Time: 11:50
# @url: http://www.lintcode.com/zh-cn/problem/strings-homomorphism/
# @Description:

class Solution:
    # @param {string} s a string
    # @param {string} t a string
    # @return {boolean} true if the characters in s
    # can be replaced to get t or false
    def isIsomorphic(self, s, t):
        # Write your code here
        if len(s) != len(t):
            return False
        s_dict = {}
        t_dict = {}
        for i in xrange(0, len(s)):
            if s_dict.get(s[i]) != t_dict.get(t[i]):
                return False
            s_dict.setdefault(s[i], i)
            t_dict.setdefault(t[i], i)

        return True


if __name__ == '__main__':
    s = Solution()
    print (s.isIsomorphic("egg", "add"))