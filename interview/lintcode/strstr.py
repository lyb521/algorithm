# -*- coding: utf-8 -*-
# @Created by PyCharm Community Edition.
# @User: leiyongbo <lyb19900227@126.com>
# @Date: 2017/7/11
# @Time: 16:25
# @url: http://www.lintcode.com/zh-cn/problem/strstr/
# @Description:

class Solution:
    """
    @param: : source string to be scanned.
    @param: : target string containing the sequence of characters to match
    @return: a index to the first occurrence of target in source, or -1  if target is not part of source.
    """

    def strStr(self, source, target):
        # write your code here

        if target == "":
            return 0
        if  source is None or target is None:
            return -1
        for i in range(0, len(source)):
            if source[i] == target[0]:
                if source[i:i + len(target)] == target:
                    return i
        return -1


if __name__ == '__main__':
    s = Solution()
    print (s.strStr("abcdabcdefg", "bcd"))
