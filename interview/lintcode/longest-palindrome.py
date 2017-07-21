# -*- coding: utf-8 -*-
# @Created by PyCharm Community Edition.
# @User: leiyongbo <lyb19900227@126.com>
# @Date: 2017/7/18
# @Time: 11:25
# @url: http://www.lintcode.com/zh-cn/problem/rotate-string/
# @Description:


class Solution:
    # @param {string} s a string which consists of lowercase or uppercase letters
    # @return {int} the length of the longest palindromes that can be built
    def longestPalindrome(self, s):
        # Write your code here
        if not s:
            return 0
        total = 0
        s_list = []
        for i in s:
            cou = s.count(i)
            if cou == len(s):
                return len(s)
            if cou >=2 and i not in s_list:
                s_list.append(i)
                total += cou / 2
        return total*2 + 1

if __name__ == '__main__':
    s = Solution()
    print (s.longestPalindrome("aaa"))