# -*- coding: utf-8 -*-
# @Created by PyCharm Community Edition.
# @User: leiyongbo <lyb19900227@126.com>
# @Date: 2017/9/25
# @Time: 15:35
# @url: http://www.lintcode.com/zh-cn/problem/missing-string/
# @Description:Given two strings, you have to find the missing string.
class Solution:
    """
    @param: : a given string
    @param: : another given string
    @return: An array of missing string
    """

    def missingString(self, str1, str2):
        # Write your code here
        if not str1:
            return []
        if not str2:
            return str1.split()
        if str1 == str2:
            return []
        str2_list = str2.split()
        print (str2_list)
        res_list = []
        for i in str1.split():
            if i not in str2_list:
               res_list.append(i)
        return res_list

if __name__ == '__main__':
    s = Solution()
    print (s.missingString("This is an example", "is example"))