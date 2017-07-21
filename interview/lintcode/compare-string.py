# -*- coding: utf-8 -*-
# @Created by PyCharm Community Edition.
# @User: leiyongbo <lyb19900227@126.com>
# @Date: 2017/7/12
# @Time: 17:36
# @url: http://www.lintcode.com/zh-cn/problem/compare-strings/
# @Description: 比较两个字符串A和B，确定A中是否包含B中所有的字符。字符串A和B中的字符都是 大写字母

class Solution:
    """
    @param A : A string includes Upper Case letters
    @param B : A string includes Upper Case letters
    @return :  if string A contains all of the characters in B return True else return False
    """
    def compareStrings(self, A, B):
        # write your code here
        a_list = list(A)
        b_list = list(B)
        b_len = len(B)
        cou = 0
        for i in b_list:
            if a_list.count(i) >= b_list.count(i):
                cou += 1
        if cou == b_len:
            return True
        else:
            return False


if __name__ == '__main__':
    s = Solution()
    print (s.compareStrings("ABCD", "ABC"))