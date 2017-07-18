# -*- coding: utf-8 -*-
# @Created by PyCharm Community Edition.
# @User: leiyongbo <lyb19900227@126.com>
# @Date: 2017/7/18
# @Time: 14:13
# @url: http://www.lintcode.com/zh-cn/problem/valid-palindrome/
# @Description:
import re
class Solution:
    # @param {string} s A string
    # @return {boolean} Whether the string is a valid palindrome
    def isPalindrome(self, s):
        # Write your code here
        if not s:
            return True
        s = re.findall('[a-zA-Z0-9]+', s)
        if "".join(s).lower() == "".join(s).lower()[::-1]:
            return True
        return False


if __name__ == '__main__':
    s = Solution()
    print  s.isPalindrome("A man, a plan, a canal: Panama" )