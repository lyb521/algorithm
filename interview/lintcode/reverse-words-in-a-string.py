# -*- coding: utf-8 -*-
# @Created by PyCharm Community Edition.
# @User: leiyongbo <lyb19900227@126.com>
# @Date: 2017/7/27
# @Time: 11:45
# @url: http://www.lintcode.com/zh-cn/problem/binary-tree-maximum-node/
# @Description:

class Solution:
    # @param s : A string
    # @return : A string
    def reverseWords(self, s):
        # write your code here
        if not s:
            return s
        str_list = filter(lambda t: t != "", s.strip().split(" "))
        str_list.reverse()
        return " ".join(str_list)


if __name__ == '__main__':
    s = Solution()
    print (s.reverseWords("How    are you?"))
