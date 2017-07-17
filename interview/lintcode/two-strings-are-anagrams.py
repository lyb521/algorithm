# -*- coding: utf-8 -*-
# @Created by PyCharm Community Edition.
# @User: leiyongbo <lyb19900227@126.com>
# @Date: 2017/7/17
# @Time: 11:39
# @url: http://www.lintcode.com/zh-cn/problem/two-strings-are-anagrams/
# @Description:

class Solution:
    """
    @param s: The first string
    @param b: The second string
    @return true or false
    """

    def anagram(self, s, t):
        # write your code here
        s_list = {}
        for i in s:
            if s_list.get(i, 0):
                index = t.find(i, s_list.get(i, 0) + 1)
            else:
                index = t.find(i)
            print index
            if index > -1:
                s_list.setdefault(i, index)
            else:
                return False
        return True


if __name__ == '__main__':
    s = Solution()
    print  s.anagram("ab", "ab")
